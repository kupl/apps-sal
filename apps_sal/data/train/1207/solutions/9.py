for _ in range(int(input())):
    c = int(input())
    p = list(map(int, input().split()))
    p.sort()
    count = 0
    for i in range(1, c):
        count += p[0] * p[i]
    print(count)
