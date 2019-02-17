#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

from PIL import Image


def save_picture(origin, output_directory='Comp', quality=20, extension='jpg'):
    origin = os.path.abspath(origin)
    output_directory = os.path.abspath(output_directory)
    try:
        os.makedirs(output_directory)
    except:
        pass

    filename = os.path.basename(origin)
    root, _ = os.path.splitext(filename)
    output_path = os.path.join(output_directory, '%s.%s' % (root, extension))

    try:
        Image.open(origin).save(
            output_path,
            optimize=True,
            quality=quality
        )
        return output_path
    except IOError as e:
        if e.strerror:
            print(origin, e.strerror)
        else:
            print(e)


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
    for path in args.files:
        save_picture(path, args.output, args.quality)
