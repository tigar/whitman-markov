'''
Generate new text from the Markov chains
'''

import pickle
import random

def make_poem(chain):
    word1 = "BEGIN"
    word2 = "WORD"
    poem = []
    while True:
        word1, word2 = word2, random.choice(chain[(word1, word2)])
        if word2 == "ENDWORD":
            break
        poem.append(word2)
    return " ".join(poem)

def main():
    chain = pickle.load(open("emerson_whitman.pkl", "rb"))


if __name__ == '__main__':
    main()
