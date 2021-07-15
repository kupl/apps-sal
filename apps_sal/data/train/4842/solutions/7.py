import random
def mutate(chromosome, p):
    return ''.join([x if random.random() > p else '10'[int(x)] for x in chromosome])
