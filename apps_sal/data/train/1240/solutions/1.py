import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


for _ in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    # print(a)
    for i in range(len(a)):
        if a[i] % 6 != 0:
            a[i] = a[i] % 6
        elif a[i] % 6 == 0:
            a[i] = 6
    # print(a)
    print(sum(a))
