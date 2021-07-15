'''Author- Akshit Monga'''
from sys import stdin,stdout
# input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[1 for x in range(n)]
    print(*arr)
