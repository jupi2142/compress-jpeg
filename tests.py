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


# "What if they send a non image file?" - DONE

# "What if the file doesn't exist?" - DONE

# "What if the file doesn't exist?" - DONE

# "I _know_ I'm gonna forget the tests sooner or later." - DONE
