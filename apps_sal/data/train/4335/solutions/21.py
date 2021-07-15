# What is an anagram? Well, two words are anagrams of each other
# if they both contain the same letters. For example:
# 'abba' & 'baab' == true ; 'abba' & 'bbaa' == true 
# 'abba' & 'abbba' == false ; 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array
# if there are none. For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) =>
# ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    w_buff = []
    w_out = []
    for w_t in words :
        if len(w_t) == len(word):
           w_buff.append(w_t)
    w_w = list(word)
    w_w.sort()
    for w_t in w_buff:
        w_buff_l = list(w_t)
        w_buff_l.sort()
        if w_buff_l == w_w :
            w_out.append(w_t)
    return w_out
