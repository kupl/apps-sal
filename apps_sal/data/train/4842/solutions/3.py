from random import random


def mutate(chromosome, p):

    def mutation(x): return '1' if x == '0' else '0'
    return ''.join([mutation(c) if random() < p else c for c in chromosome])
