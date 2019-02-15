#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from PIL import Image


def get_pictures(path):
    path = os.path.abspath(path)
    try:
        for picture in os.listdir(path):
            absolute_path = os.path.join(path, picture)
            if os.path.isfile(absolute_path):
                yield picture
    except OSError:
        yield path


def compressor_factory(quality, output_directory_prefix='compressed'):
    def inner(picture):
        directory = os.path.dirname(picture)
        output_directory = os.path.join(directory, output_directory_prefix)
        basename = os.path.basename(picture)

        try:
            os.makedirs(output_directory)
        except:
            pass

        Image.open(picture).save(
            os.path.join(output_directory, basename),
            optimize=True,
            quality=quality
        )
    return inner


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='compress-jpeg',
        description="Compress image files to jpeg"
    )

    parser.add_argument('path',
                        type=str,
                        help='Directory or file that contains the picture[s]')
    parser.add_argument("-p",
                        "--prefix",
                        type=str,
                        help="output prefix",
                        default='compressed')
    parser.add_argument("-q",
                        "--quality",
                        type=int,
                        help="quality",
                        default=20)

    args = parser.parse_args()
    map(compressor_factory(args.quality, args.prefix), get_pictures(args.path))
