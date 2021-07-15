import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
for _ in range(int(input())):
    n = int(input())
    k = 0
    for i in range(n//2+1):
        for i in range(k):
            print(" ", end ="")
        print("*")
        k = k+1
    #print("*")
    k = k-2
    for i in range(n//2):
        for i in range(k):
            print(" ",end="")
        print("*")
