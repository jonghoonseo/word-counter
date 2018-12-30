import codecs
import csv
import os

from flask import Flask, flash, jsonify, redirect, render_template, request, \
                  url_for
from werkzeug import secure_filename

import word_counter


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    word_statistics = {}

    if request.method == 'POST':
        word_counter.set_pattern(request.form['include_pattern'],
                                 request.form['exclude_pattern'])

        file = request.files.get('file', None)
        if file:
            csv_reader = csv.DictReader(
                codecs.iterdecode(file.stream, 'utf-8'))
            for index, row in enumerate(csv_reader):
                word_statistics = word_counter.count(
                    word_statistics,
                    row[request.form['column_name']],
                    index)

            sorted_word_statistics = sorted(
                word_statistics,
                key=lambda k: len(word_statistics[k]),
                reverse=True)

            return render_template('result.html',
                                   statistics=word_statistics,
                                   sorted_statistics=sorted_word_statistics)
        else:
            return redirect(url_for('index'))


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug = True)