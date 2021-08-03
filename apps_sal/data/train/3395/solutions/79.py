import re


def remove_duplicate_words(s):
    sx = []
    for i in s.split():
        if i not in sx:
            sx.append(i)
    return " ".join(sx)
