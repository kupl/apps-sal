from random import random
def mutate(chromosome, p):
    opp = {'0':'1','1':'0'}
    return ''.join(opp[x] if random() < p else x for x in chromosome)
