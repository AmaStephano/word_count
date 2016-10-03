# put your code here.
def word_counter(filename):
    with open(filename) as word_file:
        word_counts = {}
        
        for line in word_file:
            words = line.strip().split(" ")
            
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

        # for word in word_counts:
        #     print word, word_counts[word]

        # for word, count in word_counts.items():
        #     print word, count

        # list unpacking and generators
        for word, count in word_counts.iteritems():
            print word, count

word_counter("test.txt")
word_counter("twain.txt")