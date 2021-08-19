for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in l:
        d[i] += 1
    print(min(d.values()))
