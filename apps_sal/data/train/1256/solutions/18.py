for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(1 for el in l if el > 2)
    c = l.count(2)
    print(c * s + s * (s - 1) // 2)
