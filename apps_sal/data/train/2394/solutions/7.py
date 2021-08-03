import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    S = input().strip()

    MIN = 0
    NOW = 0
    for s in S:
        if s == "(":
            NOW += 1
        else:
            NOW -= 1
            MIN = min(NOW, MIN)

    print(-MIN)
