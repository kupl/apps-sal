import re


def split_without_loss(s, split_p):
    return [i for i in re.sub(''.join([i for i in split_p if i != '|']), split_p, s).split('|') if i]
