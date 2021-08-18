
t = int(input())

for testCase in range(t):
    n, m = list(map(int, input().split()))
    chakra = [0] * 101
    for i in range(n):
        c, l = list(map(int, input().split()))
        chakra[l] += c
    for i in range(m):
        p, l = list(map(int, input().split()))
        chakra[l] -= p
    boost = 0
    for c in chakra:
        boost += max(0, -c)
    print(boost)
