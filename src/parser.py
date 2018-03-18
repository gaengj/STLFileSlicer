"""Auteurs : Louis Lagier, Jean-Baptiste Gaeng."""
"""Module contenant des outils pour lire des fichiers binaires."""

import struct

from geometry import Triangle, Vertex
from utils import extremums


class BinaryParser(object):
    """Lit des types Python à partir d'octets."""
    def __init__(self, file):
        """Constructeur de la classe."""
        self.file = file

    def _read(self, format_, size):
        """Lit un type Python à partir d'octets."""
        raw = self.file.read(size)
        data = struct.unpack(format_, raw)
        if len(data) == 1:
            return data[0]
        else:
            return data

    def read_bytes(self, size):
        """Lit un nombre d'octets donné en argument."""
        return self.file.read(size)

    def read_uint16(self):
        """Lit un entier non-signé codé sur 16 bits (= 2 octets)."""
        return self._read('<H', 2)

    def read_uint32(self):
        """Lit un entier non-signé codé sur 32 bits (= 4 octets)."""
        return self._read('<I', 4)

    def read_float(self, number=1):
        """Lit un ou plusieurs nombre(s) flottant(s)."""
        return self._read('<{}f'.format(number), 4 * number)


def parse_stl(filename):
    """Parse un fichier STL."""
    data = {
        'triangles': [],

        # Extremums
        'xmin': float('inf'),
        'xmax': float('-inf'),
        'ymin': float('inf'),
        'ymax': float('-inf'),
        'zmin': float('inf'),
        'zmax': float('-inf'),
    }

    file = open(filename, 'rb')
    parser = BinaryParser(file)
    parser.read_bytes(80)
    data['num_triangles'] = parser.read_uint32()
    print('Nombre de triangles :', data['num_triangles'])

    for _ in range(data['num_triangles']):
        # Vecteur normal
        parser.read_float(3)
        vertices = []
        for _ in range(3):
            vertex = Vertex(parser.read_float(3))
            data['xmin'], data['xmax'] = extremums(
                data['xmin'], data['xmax'], vertex.x)
            data['ymin'], data['ymax'] = extremums(
                data['ymin'], data['ymax'], vertex.y)
            data['zmin'], data['zmax'] = extremums(
                data['zmin'], data['zmax'], vertex.z)
            vertices.append(vertex)
        # Attribute byte count
        parser.read_uint16()
        triangle = Triangle(vertices)
        data['triangles'].append(triangle)
    file.close()

    return data
