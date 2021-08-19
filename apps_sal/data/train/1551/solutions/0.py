# cook your dish here
import re
t = int(input())
while(t > 0):
    s = list(input().split(' '))
    if("not" in s):
        print("Real Fancy")
    else:
        print("regularly fancy")
    t = t - 1
