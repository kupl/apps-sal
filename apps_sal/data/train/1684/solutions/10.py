from sys import stdin,stdout
from collections import defaultdict 
t=int(stdin.readline())
for _ in range(t):
    n=int(stdin.readline())
    for i in range(1,n+1):
        stdout.write(str(i)+' ')
    stdout.write('\n')
