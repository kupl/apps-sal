import re


def how_many_bees(b):
    return 0 if not b else sum([len(re.findall('bee', ''.join(i + [' '] + i[::-1]))) for i in b] + [len(re.findall('bee', ''.join(i + tuple(' ') + i[::-1]))) for i in zip(*b)])
