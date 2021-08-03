import re


def frogify(s):
    delimiters = set([".", "!", "?"])
    sentences = re.split("([\!\.\?])", re.sub("[,\;\)\(-]", "", s))
    res = []
    sentence = ""

    for item in sentences:
        if item in delimiters:
            res.append(" ".join(sentence.split(" ")[::-1]) + item)
            sentence = ""
        elif item:
            sentence += re.sub("\s+", " ", item).strip()

    return " ".join(res)
