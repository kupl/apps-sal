from functools import reduce 

def words_to_marks(s):
    
    return reduce((lambda x,y: x+y), map((lambda x: ord(x) - 96), list(s)))
