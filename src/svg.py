# pylint: disable=invalid-name

"""Auteurs : Louis Lagier, Jean-Baptiste Gaeng."""
"""Fonctions utilitaires pour générer un fichier SVG."""


def header(width, height):
    """Génère un en-tête SVG avec les dimensions fournies."""
    return '<svg width="{}" height="{}">\n'.format(width, height)


def line(x1, y1, x2, y2):
    """Génère une ligne SVG avec les coordonnées fournies."""
    return ('<line x1="{}" y1="{}" x2="{}" y2="{}" '
            'style="stroke:rgb(255,0,0);stroke-width:0.2" />\n'
            .format(x1, y1, x2, y2))


def footer():
    """Génère un pied-de-page SVG."""
    return '</svg>\n'
