for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {i: 0 for i in range(1, 9)}
    for i in a:
        d[i] = d[i] + 1
    print(min(d.values()))
