"""Count word appearance with given pattern"""

from collections import defaultdict
import re


INCLUDE_PATTERN = None
EXCLUDE_PATTERN = None


def set_pattern(include_pattern, exclude_pattern):
    global INCLUDE_PATTERN, EXCLUDE_PATTERN
    INCLUDE_PATTERN = include_pattern
    EXCLUDE_PATTERN = exclude_pattern


def count(statistics, sentence, row_index):
    """From the given sentence, make stores row_index to the word
    buckets

    Args:
        statistics: a previous count dictionary
        sentence: a given sentence to preceed
        row_index: the index of this sentence

    Returns:
        a new updated count dictionary
    """
    if not statistics:
        statistics = defaultdict(lambda: [])

    if INCLUDE_PATTERN and not re.search(INCLUDE_PATTERN, sentence):
        return statistics

    unique_words = set()
    for word in sentence.split():
        # normalize word: 1. to lower 2. remove punctuation
        word = word.lower()
        word = re.sub(r'[^\w\s]', '', word)

        # check if this is in exclude pattern or already checked
        if ((EXCLUDE_PATTERN and re.match(
                EXCLUDE_PATTERN, word, re.IGNORECASE)) or
                word in unique_words or
                not word):
            continue

        unique_words.add(word)
        statistics[word].append(row_index)

    return statistics
