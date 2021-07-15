import re

def scramble_words(words):
    def sort_letters(match):
        s = match.group()
        letters = iter(sorted(filter(str.isalpha, s[1:-1])))
        return s[0] + "".join(next(letters) if c.isalpha() else c for c in s[1:-1]) + s[-1]
    return re.sub(r'[a-z][^\s]*[a-z]', sort_letters, words)
