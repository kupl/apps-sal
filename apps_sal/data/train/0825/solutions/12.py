"""
BBG Sticks (Set II)
Created on Mar 10, 2012
@author: Andy Huang
"""
t = eval(input())
while t:
    t -= 1
    n = eval(input())
    n -= 2
    print(2 ** n + 1)
