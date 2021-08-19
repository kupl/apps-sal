import re


def triple_double(num1, num2):
    triples = re.findall('(\\d)\\1{2}', str(num1))
    doubles = re.findall('(\\d)\\1{1}', str(num2))
    return len(set(triples) & set(doubles))
