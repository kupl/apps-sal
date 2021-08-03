import sys
import math
from collections import defaultdict, Counter

input = sys.stdin.readline


def print(x):
    sys.stdout.write(str(x) + "\n")

# sys.stdout=open("CP2/output.txt",'w')
# sys.stdin=open("CP2/input.txt",'r')


# m=pow(10,9)+7
t = int(input())
for i in range(t):
    a, b, n = map(int, input().split())
    c = a ^ b
    c1 = bin(c).lstrip('0b')
    c1 = list(c1.rjust(max(len(bin(a)), len(bin(b))) - 2, '0'))
    # print(c1)
    for j in range(len(c1)):
        if c1[j] == '0':
            c1[j] = '1'
        else:
            c1[j] = '0'
    c1 = int(''.join(c1), 2)
    # print(c1,end=' ')
    l = [a, b, max(c, c1)]
    # if a==b:
    #   l[2]=1
    # n1=n
    # a1,b1=a,b
    ans = l[(n - 1) % 3]
    print(ans)
    # while n1-2:
    #   n1-=1
    #   c=a^b
    #   print(c,end=' ')
    #   a,b=b,c
    # print()
    # a,b=a1,b1
    # while n-2:
    #   n-=1
    #   c1=bin(a^b).lstrip('0b')
    #   c1=list(c1.rjust(max(len(bin(a)),len(bin(b)))-2,'0'))
    #   # print(c1)
    #   for j in range(len(c1)):
    #       if c1[j]=='0':
    #           c1[j]='1'
    #       else:
    #           c1[j]='0'
    #   c1=int(''.join(c1),2)
    #   print(c1,end=' ')
    #   a,b=b,c1
    #   # print(max(c,int(''.join(c1),2)))
