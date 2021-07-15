from itertools import groupby
def run_length_encoding(s):
    encoded_s = []

    #define key function that returns first char as key
    key = lambda x: x[0]
    
    for k, g in groupby(s, key):
        encoded_s.append([len(list(g)), k])
    
    return encoded_s

