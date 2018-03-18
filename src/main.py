#!/usr/bin/env python3

"""Auteurs : Louis Lagier, Jean-Baptiste Gaeng."""
"""Module principal du programme."""

import argparse
import os
import sys

from parser import parse_stl
from slicer import write_slices


def main():
    """Point d'entrée du programme."""
    parser = argparse.ArgumentParser(description='Tranche un fichier STL.')
    parser.add_argument('-s', '--slices', type=int, default=16,
                        help='un nombre de tranches')
    parser.add_argument('-o', '--output', default='output',
                        help='le répertoire ou écrire les tranches')
    parser.add_argument('filename', help='un fichier STL à trancher')
    args = parser.parse_args()

    filename = args.filename
    if not os.path.exists(filename):
        print('error: file {} does not exist.'.format(filename))
        sys.exit(1)

    if not os.path.exists(args.output):
        os.mkdir(args.output)

    data = parse_stl(filename)
    write_slices(data, args.slices, args.output)


if __name__ == '__main__':
    main()
