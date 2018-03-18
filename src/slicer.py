# pylint: disable=invalid-name

"""Auteurs : Louis Lagier, Jean-Baptiste Gaeng."""
"""Fonctions pour trancher un modèle 3D."""

import itertools
import os

from geometry import Vertex, intersect
from svg import header, line, footer


def write_slices(data, num_slices, output_path):
    """Découpe le modèle 3D en tranches et écrit le résultat dans des fichiers
    SVG.

    """
    height = abs(data['zmax'] - data['zmin'])
    slices = [data['zmin'] + i * height / (num_slices+1)
              for i in range(1, num_slices+1)]

    for i, height in enumerate(slices):
        print('Création de la tranche numéro', i)

        path = os.path.join(output_path, 'slice_{}.svg'.format(i))
        file_ = open(path, 'w')

        svg_width = int(abs(data['xmax'] - data['xmin'])) + 10
        svg_height = int(abs(data['ymax'] - data['ymin'])) + 10
        file_.write(header(svg_width, svg_height))

        for triangle in data['triangles']:
            segment = []
            for side in itertools.combinations(triangle.vertices, 2):
                if intersect(height, side):
                    xa, ya, za = side[0].position
                    xb, yb, zb = side[1].position
                    if zb-za != 0:
                        c = (height-za)/(zb-za)
                        vertex = Vertex((xa+c*(xb-xa), ya+c*(yb-ya), height))
                        segment.append(vertex)
                    else:
                        print('divide by 0')
            if len(segment) > 0:
                file_.write(line(
                    segment[0].x-data['xmin'], segment[0].y-data['ymin'],
                    segment[1].x-data['xmin'], segment[1].y-data['ymin']))

        file_.write(footer())
        file_.close()
