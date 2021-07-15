from functools import *

def get_average(marks):
    nth = len(marks)
    aggregate = reduce(lambda x,y : x+y,marks)
    return aggregate // nth

