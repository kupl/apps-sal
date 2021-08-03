for _ in range(int(input())):
    n = input()
    ar = list(map(int, input().split()))
    ar.sort()
    print(ar[-1] * ar[-2], ar[0] * ar[1])
