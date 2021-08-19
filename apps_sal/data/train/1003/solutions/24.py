def go():
    (n, m) = list(map(int, input().split()))
    d = [0] * 101
    for i in range(n):
        (c, l) = list(map(int, input().split()))
        d[l] += c
    for i in range(m):
        (c, l) = list(map(int, input().split()))
        d[l] -= c
    print(sum((-i for i in d if i < 0)))


for t in range(eval(input())):
    go()
