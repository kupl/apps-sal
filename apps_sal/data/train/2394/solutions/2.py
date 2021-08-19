# for _ in range(1):
for _ in range(int(input())):
    # a, b = map(int, input().split())
    n = int(input())
    # arr = list(map(int, input().split()))
    s = input()
    bal = 0
    minbal = 0
    for i in range(n):
        if s[i] == ')':
            bal -= 1
        else:
            bal += 1
        minbal = min(minbal, bal)
    print(-minbal)
