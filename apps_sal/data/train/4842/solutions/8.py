import random
import string
tbl = string.maketrans('01', '10')


def mutate(chromosome, p):
    return ''.join((c.translate(tbl) if random.random() <= p else c for c in chromosome))
