import re


def remove_duplicate_words(s):
    s_list = []
    s_2 = ''
    all = s.split()
    for word in s.split():
        if word not in s_list:
            s_2 += ' ' + word
            s_list.append(word)
    return s_2.strip()
