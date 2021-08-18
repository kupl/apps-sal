import sys
def input(): return sys.stdin.readline().rstrip('\r\n')


for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in a:
        if i & 1 == 0:
            ans += i
    print(ans)
