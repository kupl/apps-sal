for _ in range(int(input())):
    n = int(input())
    l = [int(c) for c in input().split()]
    t = [0 for i in range(8)]
    for i in l:
        t[i - 1] += 1
    print(min(t))
