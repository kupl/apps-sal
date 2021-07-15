""" 
    When you do know almost nothing about bitwise operators except of their existence...
    ...and that you make by chance a good guess... 
"""
def mystery(n):  return n ^ (n//2)


"""
    Then you do some pattern recognition to solve the kata! 
"""
import re, string
TABLE = string.maketrans('01', '10')

def mystery_inv(n):
    return int(''.join( a+b.translate(TABLE)+c for a,b,c in re.findall(r'(1)(0*1?)(0*)', bin(n)[2:]) ) or '0', 2)
    

def name_of_mystery(): return "Gray code"
