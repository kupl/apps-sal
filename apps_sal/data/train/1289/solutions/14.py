""" 
Chef at Gym
Created on Mar 3, 2012

@author: Andy Huang
"""
t = eval(input())
moi = []
ans = 1
mul = 3
i = 75
moi.append(1)
moi.append(1)
while i:
    ans *= mul
    mul += 2
    moi.append(ans)
    i -= 1
while t:
    n = eval(input())
    print(moi[n])
    t -= 1
