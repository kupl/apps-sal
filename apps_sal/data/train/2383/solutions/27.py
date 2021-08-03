import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a

    a *= 2
    ans = max(a, b)**2
    print(ans)
