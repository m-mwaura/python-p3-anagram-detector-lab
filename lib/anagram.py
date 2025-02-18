# your code goes here!
#import ipdb

class Anagram:
    #ipdb.set_trace()
    def __init__(self, word):
        self.word = word.lower()
        
    def match(self, word_list):
        sorted_word = sorted(self.word)

        matches = [word for word in word_list if sorted(word.lower()) == sorted_word]
        
        return matches
