#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

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

        try:
            Image.open(picture).save(
                os.path.join(output_directory, basename),
                optimize=True,
                quality=quality
            )
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
    pictures = map(os.path.abspath, args.files)
    map(compressor_factory(args.quality, args.prefix), pictures)
