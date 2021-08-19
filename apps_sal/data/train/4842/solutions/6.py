import random


def mutate(chromosome, p):
    return ''.join((d if random.random() >= p else str(int(not int(d))) for d in chromosome))
