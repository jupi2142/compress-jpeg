#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import shutil
from functools import wraps
from uuid import uuid4

import compress_jpeg


def announce(f):

    @wraps(f)
    def inner(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)

    return inner


@announce
def argument_directory():
    directory_path = '/tmp/' + uuid4().hex
    os.makedirs(directory_path)
    assert compress_jpeg.save_picture(directory_path) is None


@announce
def argument_non_image():
    non_image_path = '/tmp/' + uuid4().hex
    file(non_image_path, 'w+').close()
    assert compress_jpeg.save_picture(non_image_path) is None


@announce
def argument_non_existent():
    non_existent_path = '/tmp/' + uuid4().hex
    assert compress_jpeg.save_picture(non_existent_path) is None


@announce
def correct_output():
    temp_folder = '/tmp/' + uuid4().hex
    os.makedirs(temp_folder)

    path = '1-001.jpg'
    new_path = os.path.join(temp_folder, '1-001.jpg')
    shutil.copy(path, new_path)

    output = '/tmp/' + uuid4().hex
    os.makedirs(output)

    assert compress_jpeg.save_picture(new_path, output) is not None
    assert path in os.listdir(output)


@announce
def inplace_replacement():
    path = '1-001.jpg'
    output = '/tmp/' + uuid4().hex
    os.makedirs(output)
    shutil.copy(path, output)
    new_path = os.path.join(output, path)

    previous_size = os.stat(new_path).st_size

    assert compress_jpeg.save_picture(new_path, None) is not None

    new_size = os.stat(new_path).st_size
    assert new_size < previous_size


argument_directory()
argument_non_image()
argument_non_existent()
correct_output()
inplace_replacement()


# "What if they send a non image file?" - DONE

# "What if the file doesn't exist?" - DONE

# "What if the file doesn't exist?" - DONE

# "I _know_ I'm gonna forget the tests sooner or later." - DONE

# "What if I just want to override the picture? What then? :hmm: Would passing
# '.' to work 'prefix' work?" Jupi thoughts. "Let's try this!"

# "We need to change how the output works. It should just be a directory/path" -
# DONE

# "I think it's time to use this in a web app"
