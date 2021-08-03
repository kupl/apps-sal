import re


def gordon(a):
    return re.sub("[EIOU]", "*", " ".join(word.upper() + "!!!!" for word in a.split()).replace("A", "@"))
