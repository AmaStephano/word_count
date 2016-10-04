
from collections import Counter
from string import punctuation
from sys import argv

def reverse_tuple(tup):

    return (tup[1], tup[0])

def reverse_and_neg_tuple(tup):

    #make number negative and sort based on that. Won't actually affect tuple your are sorting.
    return (-1 * tup[1], tup[0])

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
        
        # word_counts.items() returns tuples of key value pairs. 
        # itemgetter sorts tuples first on count then key
        #for word, count in sorted(word_counts.items(), key=itemgetter(1,0)):
        # for word, count in sorted(word_counts.items(),
        #                           reverse=True,
        #                           key=reverse_tuple):
        for word, count in sorted(word_counts.items(),
                                  key=reverse_and_neg_tuple):
            print word, count

word_file = argv[1]
word_counter(word_file)