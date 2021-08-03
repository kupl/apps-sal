# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().rstrip().split())
        print(N + M - 1)
except:
    pass
