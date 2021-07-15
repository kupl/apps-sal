import re

def reverse_words(text):
    list = re.split(r'(\s+)', text)
    res = ""
    for w in list:
        for i in range(len(w), 0, -1):
            res += w[i - 1]
    return res
