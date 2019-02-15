#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

from PIL import Image


def compressor_factory(quality, output_directory='compressed'):
    output_directory = os.path.abspath(output_directory)

    def inner(picture):
        picture = os.path.abspath(picture)
        filename = os.path.basename(picture)
        root, extension = os.path.splitext(filename)
        output_path = os.path.join(output_directory, '%s.jpg' % root)

        try:
            os.makedirs(output_directory)
        except:
            pass

        try:
            Image.open(picture).save(
                output_path,
                optimize=True,
                quality=quality
            )
            return output_path
        except IOError as e:
            if e.strerror:
                print(picture, e.strerror)
            else:
                print(e)
    return inner


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='compress-jpeg',
        description="Compress image files to jpeg"
    )

    parser.add_argument("files", help="file[s] to convert", nargs='+')
    parser.add_argument("-o",
                        "--output",
                        type=str,
                        help="Output directory",
                        default='compressed')
    parser.add_argument("-q",
                        "--quality",
                        type=int,
                        help="quality",
                        default=20)

    args = parser.parse_args()
    map(compressor_factory(args.quality, args.output), args.files)
