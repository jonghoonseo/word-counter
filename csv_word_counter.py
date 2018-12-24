"""Count the number of words with a csv file

Usage:
    python csv_word_counter.py data_science_bootcamps.csv \
        --column_name=MESSAGES \
        --include_pattern='PhD|12'\
        --exclude_pattern='\d+'
    : this read 'MESSAGES' column from data_science_bootcamps.csv,
    and cound rows which include 'PhD' or '12' and
    excludes number words.
"""

import argparse
import csv
import os

import word_counter


class Error(Exception):
    """Exception class"""
    pass


def _parse_args():
    parser = argparse.ArgumentParser(description='Word counter')
    parser.add_argument('file_path', type=str, nargs='?',
                        help='a file path to proceed')
    parser.add_argument('--column_name', action='store', default='messages',
                        help='A column name to make statistics')
    parser.add_argument('--include_pattern', action='store',
                        help='Include filter')
    parser.add_argument('--exclude_pattern', action='store',
                        help='Exclude filter')

    args = parser.parse_args()

    return args


def _main(args):
    if not args.file_path or not os.path.exists(args.file_path):
        raise Error('Invalid file error')

    word_counter.set_pattern(args.include_pattern, args.exclude_pattern)

    word_statistics = {}
    with open(args.file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for i, row in enumerate(csv_reader):
            word_statistics = word_counter.count(word_statistics,
                                                 row[args.column_name],
                                                 i)

    print(word_statistics)


if __name__ == "__main__":
    PARSED_ARGS = _parse_args()
    _main(PARSED_ARGS)
