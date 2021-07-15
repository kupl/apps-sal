from random import *

def mutate(chromosome, p):
    def mutate(gene): return '1' if gene=='0' else '0'
    return "".join([(mutate(x) if random() <= p else x) for x in chromosome])

