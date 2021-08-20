try:
    t = int(input())
    for i in range(t):
        (n, k) = map(int, input().split())
        l = [int(x) for x in input().split()]
        print(abs(max(l) + k - (min(l) - k)))
except EOFError:
    pass
