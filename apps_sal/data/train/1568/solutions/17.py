for _ in range(int(input())):
    n = int(input())
    l = [*map(int, input().split())]
    print(sum((1 for e in l if e >= n / 2)))
