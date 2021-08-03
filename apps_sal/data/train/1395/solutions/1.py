# cook your dish here
#import sys
# input=sys.stdin.readline
# m=int(input())
for nt in range(int(input())):
    a, b = list(map(int, input().split()))
    n = abs(a - b)
    cnt = 0
    for i in range(1, int(n**(1 / 2)) + 1):
        if n % i == 0:
            if n / i == i:
                cnt += 1
            else:
                cnt += 2
    print(cnt)
