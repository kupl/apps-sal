import math

def converter(mpg):
    res =  mpg * 0.354006
    
    s = str(res)
    dot = s.index('.')
    if [len(s) -1] =='0':
      return float(s[:dot + 1])
    else:
      return round(res,2)

