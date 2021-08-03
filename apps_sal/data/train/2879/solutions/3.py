import re


def could_be(original, another):
    a = re.sub(r'[,.!;:?]', ' ', another.lower())
    print(a)

    return a.strip() > '' and set(a.split()) <= set(original.lower().split())
