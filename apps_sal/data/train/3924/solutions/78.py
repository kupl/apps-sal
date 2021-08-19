import re


def reverse_words(text):
    stuff = re.split('(\s+)', text)
    print(stuff)
    cat = list()
    for words in stuff:
        reverse = words[::-1]
        cat.append(reverse)
    dog = ''.join(cat)

    return dog

  # go for it
