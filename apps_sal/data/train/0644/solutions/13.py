for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = sum(arr)
    if x % n == 0:
        print('Yes')
    else:
        print('No')
