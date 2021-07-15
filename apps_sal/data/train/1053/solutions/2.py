from sys import*
input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    l.sort()
    print(l.index(1))

