#----------------------------------------#
# Title: Trigrams.py
# Initial File
# Claire Yoon,2019-02-03,New file
#----------------------------------------#

"""
build up the trigrams dict from the list of words

returns a dict with:
   keys: word pairs
   values: list of followers
"""

import sys
import string
import random
# from string import maketrans

def read_in_data(filename):
    objFile = open(filename, "r")
    strData = objFile.read()
    # return text in one line
    return strData

def make_words(in_data):
    in_data.replace(" *** START OF THIS PROJECT GUTENBERG EBOOK",'')
    in_data = in_data.translate({ord(c): " " for c in "\"!@#$%^&*()[]{};:,/<>?\|~-=_+"})
    words = in_data.split()
    # print(words)
    return words

def build_trigram(words):

    trigrams = {}
    # why -2?: last two words would not have next one.
    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        val = trigrams.get((pair[0], pair[1]))

        if val is None :
            val = [follower]
        else :
            val.append(follower)
        trigrams.update({(pair[0], pair[1]): val})

    # build up the dict here!
    # print(trigrams)
    return trigrams

def build_text(word_pairs):
    # returns a number between 0 and len(word_pairs) - 1
    starting_point = random.randint(0,len(word_pairs) - 1)
    # get word list of key of starting point
    start_word = list(word_pairs.keys())[starting_point]
    new_text = start_word[0] + ' ' + start_word[1]
    # while the pair has next word
    while(True):
        word_list = new_text.split()
        new_tuple = (word_list[-2] , word_list[-1])
        # if the tuple is one of the keys of word_pairs:
        if new_tuple in word_pairs.keys():
            word_values = word_pairs.get(new_tuple)
            rand_val = random.randint(0,len(word_values) - 1)
            join_word = word_values[rand_val]
            new_text = new_text + ' ' + join_word

            # print(new_text)
        # else: terminate the function
        else:
            break
    return new_text

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)