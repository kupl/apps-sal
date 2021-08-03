import sys
def input(): return sys.stdin.readline().strip()


T = int(input())
for i in range(T):
    a, b, n = list(map(int, input().split()))
    if n % 3 == 0:
        print(a)
    elif n % 3 == 1:
        print(b)
    else:
        print(a ^ b)
