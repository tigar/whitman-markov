import nltk
import sys
import fileinput
import pickle

def parse_corpus(path_to_file):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open(path_to_file)
    data = fp.read()
    all_sentences = tokenizer.tokenize(data)
    tagged_sentences = ["BEGIN WORD " + s.lower() + " ENDWORD" for s in all_sentences]
    return tagged_sentences

def make_trigrams(sentence):
    if len(sentence) < 3:
        return
    for i in range(len(sentence) - 2):
        yield (sentence[i], sentence[i+1], sentence[i+2])

def make_chain(sentences):
    chain = {}
    for sentence in sentences:
        split_sentence = sentence.split()
        for word1, word2, word3 in make_trigrams(split_sentence):
            key = (word1, word2)
            if key in chain:
                chain[key].append(word3)
            else:
                chain[key] = [word3]
    pickle.dump(chain, open("chain.pkl", "wb"))

def main():
    whitman_sentences = parse_corpus("whitmanCopy.txt")
    make_chain(whitman_sentences, chain)




if __name__ == '__main__':
    main()
