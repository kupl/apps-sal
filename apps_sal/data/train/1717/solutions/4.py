import re


def top_3_words(text):
    re_non_valid = re.compile("[^a-z' ]")
    re_chars = re.compile('[a-z]')
    text = text.lower()
    text = ' '.join([x for x in re_non_valid.sub(' ', text).split() if re_chars.search(x)])
    words = {}
    top = {}
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        top[word] = words[word]
        if len(top) > 3:
            top.pop(min(top, key=top.get))
    return sorted(top, key=top.get, reverse=True)
