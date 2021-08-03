import re


def alan_annoying_kid(sentence):
    if "didn't" in sentence:
        s = re.search(r"didn't (.)+\.", sentence)
        s2 = 'did ' + sentence.split(' ')[3] + ' it'
        return "I don't think you {} today, I think you {}!".format(s.group()[:-1], s2)
    else:
        s = sentence.split(' ')[2][:-2]
        s1 = ' '.join(sentence.split(' ')[2:])[:-1]
        s2 = "didn't " + s + ' at all'
        return "I don't think you {} today, I think you {}!".format(s1, s2)
