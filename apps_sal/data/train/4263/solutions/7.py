import re


def apparently(string):
    return re.sub('(and|but)(?!(\w)| apparently( +|$))', '\g<0> apparently', string)
