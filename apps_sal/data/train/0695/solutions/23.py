n = int(input())
for _ in range(n):
    (a, b, c) = [int(i) for i in input().split()]
    l = list(range(0, c + 1))
    d = 0
    for i in range(0, len(l)):
        if a ^ l[i] < b ^ l[i]:
            d = d + 1
    print(d)
