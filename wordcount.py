
from collections import Counter
from string import punctuation
from sys import argv

def word_counter(filename):
    with open(filename) as word_file:
        # entire file as one string
        file_text = word_file.read()
        # split without arg to split on whitespace and newline
        words = file_text.strip().split()

        # need to loop thru index since strings are immutable        
        for i, word in enumerate(words):
            words[i] = word.lower().strip(punctuation)

        # Counter takes iterable, counts each time each thing occurs in iterable
        word_counts = Counter(words)
        
        for word, count in sorted(word_counts.items()):
            print word, count

word_file = argv[1]
word_counter(word_file)