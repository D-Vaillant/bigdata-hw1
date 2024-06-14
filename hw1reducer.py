#!/usr/bin/env python
from itertools import groupby
from operator import itemgetter
import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, sep='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(sep, 1)


def main(total_words: float, sep='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, sep=sep)

    # groupby groups multiple word-count pairs by word
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            mle = sum(int(count) for _, count in group)/total_words
            print(f"{current_word}{sep}{mle}")
        except ValueError:
            # count was not a number, so silently discard this item
            pass


if __name__ == "__main__":
    total_words = float(sys.argv[1])
    main(total_words)
