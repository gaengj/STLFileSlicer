"""Auteurs : Louis Lagier, Jean-Baptiste Gaeng."""
"""Module contenant des fonctions utilitaires."""


def extremums(minimum, maximum, value):
    """Retourne les valeurs minimum et maximum."""
    minimum = min(minimum, value)
    maximum = max(maximum, value)
    return minimum, maximum
