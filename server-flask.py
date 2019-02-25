#!/usr/bin/python
# coding: utf-8
import json
import urllib2
from hashlib import md5

from flask import Flask, request, send_file

from compress_jpeg import save_picture

app = Flask(__name__)


@app.route('/')
def entry_point():
    try:
        quality = int(request.args.get('quality', 20))
        url = request.args['url']
    except KeyError as e:
        return e


    filedata = urllib2.urlopen(url)

    datatowrite = filedata.read()
    url_hash = md5(url).hexdigest()
    original_file_path = '/tmp/%s' % url_hash

    with open(original_file_path, 'wb') as f:
        f.write(datatowrite)

    new_file_path = save_picture(original_file_path, '/tmp/Comp', quality)
    return send_file(new_file_path, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
