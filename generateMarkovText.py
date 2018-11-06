'''
Generate new text from the Markov chains
'''

import pickle
import random
import string

def make_trigram_poem(chain):
    word1 = "BEGIN"
    word2 = "WORD"
    poem = []
    while True:
        word1, word2 = word2, random.choice(chain[(word1, word2)])
        if word2 == "ENDWORD":
            break
        poem.append(word2)
    return " ".join(poem)

def make_bigram_poem(chain):
    word = "BEGIN"
    poem = []
    while True:
        word = random.choice(chain[word])
        if word == "ENDWORD":
            break
        poem.append(word)
    return ''.join([('' if val in string.punctuation else ' ') + val for val in poem])

def main():
    chain = pickle.load(open("emerson_whitman.pkl", "rb"))
    make_bigram_poem(chain)


if __name__ == '__main__':
    main()
