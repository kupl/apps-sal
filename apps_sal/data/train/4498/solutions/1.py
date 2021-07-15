from functools import reduce
def solution(roman):
    d={'I':1, 'V':5 ,'X':10, 'L':50 ,'C':100, 'D':500,'M':1000}
    
    return reduce(lambda x,y: x+y if x>=y else y-x , (d[c] for c in roman))

