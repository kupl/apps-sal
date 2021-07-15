from random import random
def mutate(ch, p):
    return ''.join([str(1-int(i)) if random()<=p else i for i in ch])
