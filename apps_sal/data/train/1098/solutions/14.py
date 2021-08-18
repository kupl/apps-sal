for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    chef = sum([lis[i] for i in range(0, n, 2)])
    other = sum(lis[i] for i in range(1, n, 2))
    print(max(chef, other))
