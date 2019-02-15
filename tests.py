#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
from uuid import uuid4

import compress_jpeg


def argument_directory():
    directory_path = '/tmp/' + uuid4().hex
    os.makedirs(directory_path)
    assert compress_jpeg.compressor_factory(20)(directory_path) is None


def argument_non_image():
    non_image_path = '/tmp/' + uuid4().hex
    file(non_image_path, 'w+').close()
    assert compress_jpeg.compressor_factory(20)(non_image_path) is None


def argument_non_existent():
    non_existent_path = '/tmp/' + uuid4().hex
    assert compress_jpeg.compressor_factory(20)(non_existent_path) is None

argument_directory()
argument_non_image()
argument_non_existent()
# "What if they send a non image file?" Jupi thought
# Decisions, decisions. What shoudl Jupi do? Jupi remembers something about
# reversible failure or some shit. Something about leaving everything not
# touched if any of them are not correct. "Hmm", Jupi thought. "I'm going to see
# how cp does it and I'll do whatever it does". So Jupi set out to figure out
# what cp does. "Good news", Jupi thought. I'm glad I don't have to call
# Image.open for every image. But Jupi still had questions. What happens if the
# first argument of cp doesn't exist?. Jupi went out back again to check. Good
# news again. It just displays the error for each missing file and just keeps
# going.

# "What if the file doesn't exist?"

# "What if the file doesn't exist?"


# "What if the directory they send has images that they want converted, but also
# miscelaneous files that the user doesn't want converted?"
# "I think it's better to stick to multiple images instead of a directory"
# "Maybe an output directory should be allowed"
# "What
