import nltk
import sys

for fname in sys.argv[1:]:
    lines = open(fname).read().strip().split('\n')
    f = open(fname, 'w')
    for line in lines:
        line_words = nltk.word_tokenize(line)
        newline = ' '.join(line_words)
        f.write(newline + '\n')
    f.close()

