from random import random
def mutate(chromosome, p):
    res = ''
    for s in chromosome:
        res += str(1 - int(s)) if random() < p else s
    return res

