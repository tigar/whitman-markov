'''
Generate the Markov chains
'''

import argparse
#import markov
import nltk
import random
import sys
import re
import pandas as pd
import numpy as np


def parse_corpus(df):
    words = []
    with open('whitman.txt', 'r') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    df['first'] = words

    second = words[1:]
    second.append("ENDWORD")
    df['second'] = second
    end_words = []
    for word in words:
        if word[-1] in ['.', '?', '!']:
            end_words.append(word)

    df = df.groupby(['first', 'second']).size().reset_index(name='freq')
    df = df.drop_duplicates()

    pivoted_df = df.pivot(index = 'first', columns= 'second', values='freq')
    sum_words = pivoted_df.sum(axis=1)
    pivoted_df = pivoted_df.apply(lambda x: x/sum_words)
    pivoted_df.to_pickle('whitman_pivoted_df.pickle')
    df.to_pickle('whitman_df.pickle')

def main():
    corpus_df = pd.DataFrame(columns = ['first', 'second', 'freq'])
    parse_corpus(corpus_df)


if __name__ == '__main__':
    main()
