# -*- coding: utf-8 -*-

import argparse

from mdnotes import commands

if __name__ == '__main__':
    parser = argparse.ArgumentParser('mdnotes')
    subparsers = parser.add_subparsers(title='commands', help='Command')

    init_parser = subparsers.add_parser('init', help='Create a new notes directory')
    init_parser.add_argument('path', type=str, help='Path to the notes directory')
    init_parser.set_defaults(func=commands.init.init)

    subparsers.add_parser('build', help='Build the project')

    subparsers.add_parser('serve', help='Start a webserver to serve the built project')

    args = parser.parse_args()
    args.func(args)
