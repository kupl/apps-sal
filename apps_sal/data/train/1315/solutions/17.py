# cook your dish here
from sys import stdin, stdout
input = stdin.readline
from collections import defaultdict as dd
import math
def geti(): return list(map(int, input().strip().split()))
def getl(): return list(map(int, input().strip().split()))
def gets(): return input()
def geta(): return int(input())
def print_s(s): stdout.write(s+'\n')

def solve():
    occur=dd(int)
    n=geta()
    a=[]
    for i in range(n):
        temp=getl()
        temp.sort(reverse=True)
        # print(temp)
        a.append(tuple(temp))
        occur[a[-1]]+=1
    ans=0
    for i in a:
        if occur[i]==1:
            ans+=1
    print(ans)



def __starting_point():
    solve()

__starting_point()
