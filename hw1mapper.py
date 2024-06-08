#!/usr/bin/env python

import sys
import re


# [\W] == [^\w] == [^0-9a-zA-Z_]. We want to filter _ as well.
pattern = re.compile("[\W_]")


def read_input(input, arity: int=1):
    for line in input:
        split_line = line.split()
        if len(split_line) < arity:  # Line has less than 1 word.
            continue
        # Strips nonalphanumeric characters.
        # Source: https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        yield pattern.sub('', split_line).lower()


def main(mode, sep='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in line:
            if mode == 'totalcount':
                word = 'TotalCount'
            print(f'{word}{sep}1')
            


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    try:
        mode = sys.argv[1]  # totalcount
    except IndexError:
        mode = 'wordcount'
    main(mode)