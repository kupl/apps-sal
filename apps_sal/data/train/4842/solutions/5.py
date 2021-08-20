from random import random


def mutate(chromosome, p):
    return ''.join(('01'[c == '0'] if random() <= p else c for c in chromosome))
