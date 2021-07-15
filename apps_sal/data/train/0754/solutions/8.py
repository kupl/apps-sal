from sys import *
input=stdin.readline
for u in range(int(input())):
    n=int(input())
    f=0
    for i in str(n):
        if(int(i)%2==0):
            f=1
            break
    print(f)

