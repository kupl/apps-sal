try:
    n = int(input())
    sm = 0
    for i in range(n):
        (a, b) = map(int, input().split())
        sm += abs(a - b) + 1
    print(sm % 1000000007)
except:
    pass
