# cook your dish here
from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ls =list(map(int,stdin.readline().split()))
    print(*ls,sep='')


