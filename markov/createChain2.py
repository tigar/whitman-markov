import argparse
#import markov
import nltk
import random
import sys
import re
import pandas as pd
import numpy as np
from numpy.random import choice
import fileinput

def parse_corpus(path_to_file):
    with open(path_to_file, 'r') as src:
        with open('whitmanParsed.txt', 'w') as dest:
            for line in src:
                if "\t\t" not in line:
                    dest.write('%s%s\n' % ("START NOW ", line.rstrip('\n')))
                else:
                    dest.write(line)

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    fp = open(path_to_file)

    data = fp.read()

    print('\n-----\n'.join(tokenizer.tokenize(data)))

def main():
    parse_corpus("whitmanCopy.txt")
    # end_words = parse_corpus(corpus_df)
    # pivot_df = pd.read_pickle('whitman_pivoted_df.pickle')
    # print(make_something("What", pivot_df, end_words))



if __name__ == '__main__':
    main()
