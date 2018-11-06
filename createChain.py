import nltk
import sys
import fileinput
import pickle
import re

'''
Tokenize each line according to the bigram model
'''
def parse_corpus_regexp(path_to_file):
    # Bigram model
    tokenized_lines = []
    pattern = re.compile('[^\t\n.,-;?!;]+|[\t\n.,-;?!;]')
    with open(path_to_file) as f:
        all_lines = f.readlines()
    for line in all_lines:
        # tokens = [x for x in re.split(r'(\W+)', line) if not re.match(r'^[ ]*$', x)]
        # tokenized_lines.append(tokens)
        split_line = line.split(' ')
        tokenized = ['BEGIN']
        tokenized += [token for all_tokens in map(pattern.findall, line.split(' ')) for token in all_tokens] # It works but this is a terrible implemntation
        tokenized.append('ENDWORD')
        tokenized_lines.append(tokenized)
    return tokenized_lines

'''
    # OLD WAY OF DOING THINGS
    # This ignores newline and tab characters and is using the trigram model
'''
def parse_corpus_nltk(path_to_file):
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

def make_bigrams(sentence):
    if len(sentence) < 2:
        return
    for i in range(len(sentence) - 1):
        yield(sentence[i], sentence[i+1])


def make_chain(sentences):
    chain = {}
    for sentence in sentences:
        for word1, word2 in make_bigrams(sentence):
            key = word1
            if key in chain:
                chain[key].append(word2)
            else:
                chain[key] = [word2]
    print(chain)
    pickle.dump(chain, open("pickles/bigramEmersonWhitman.pkl", "wb"))

def main():
    sentences = parse_corpus_regexp("corpuses/allPoems.txt")
    print(sentences)
    make_chain(sentences)

    # For testing
    # sentences = parse_corpus("gutenberg_poems.txt")
    # make_chain(sentences)



if __name__ == '__main__':
    main()
