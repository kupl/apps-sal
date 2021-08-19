for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    x = [i if i in x else 0 for i in range(n)]
    print(*x)
