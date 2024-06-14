#!/usr/bin/env python
import sys
import re

# [\W] == [^\w] == [^0-9a-zA-Z_]. We want to filter _ as well.
pattern = re.compile(r"[\W_]")


def read_input(input, arity: int=1) -> list[str]:
    for line in input:
        word_list: list[str] = line.split()
        if len(word_list) < arity:  # Line has less than 1 word.
            continue
        # Strips nonalphanumeric characters.
        # Source: https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        yield word_list


def main(mode: str, sep='\t') -> None:
    # iterates through lines, then words
    # if we're just doing a totalcount, count words
    # otherwise
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # tab-delimited; the trivial word count is 1
        for word in line:
            word = pattern.sub('', word).lower()
            # skip empty words
            if word == '':
                continue
            if mode == 'totalcount':
                word = 'TotalCount'
            print(f'{word}{sep}1')
            

# how to test locally in Bash/Linux: cat  | python mapper.py
# or invoked directly, using Ctrl-D to end
# or python mapper.py < file.txt
if __name__ == "__main__":
    if '-t' in sys.argv:
        mode = 'totalcount'
    else:
        mode = 'wordcount'  # ignored by main

    main(mode)
