# pylint: disable=invalid-name

"""Auteurs : Louis Lagier, Jean-Baptiste Gaeng."""
"""Module contenant des classes et fonctions pour représenter et manipuler
des objets géométriques.

"""


class Vertex(object):
    """Représente un point dans un espace en 3D."""
    def __init__(self, position):
        """Constructeur de la classe."""
        self.position = position

    @property
    def x(self):
        """Getter pour la coordonnée x."""
        return self.position[0]

    @property
    def y(self):
        """Getter pour la coordonnée y."""
        return self.position[1]

    @property
    def z(self):
        """Getter pour la coordonnée z."""
        return self.position[2]

    def __str__(self):
        return '<Vertex(x={}, y={}, z={})>'.format(self.x, self.y, self.z)


class Triangle(object):
    """Représente un triangle."""
    def __init__(self, vertices):
        """Constructeur de la classe."""
        self.vertices = vertices

    def __str__(self):
        return '<Triangle(vertices=[{}])>'.format(
            ', '.join([str(vertex) for vertex in self.vertices])
        )


def intersect(height, segment):
    """Teste si un segment coupe un plan horizontal de hauteur `height`."""
    if segment[0].z < height and segment[1].z < height:
        return False
    if segment[0].z > height and segment[1].z > height:
        return False
    return True
