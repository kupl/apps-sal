import re


def could_be(original, another):
    a = re.sub('[,.!;:?]', ' ', another.lower())
    print(a)
    return a.strip() > '' and set(a.split()) <= set(original.lower().split())
