for i in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    print(arr[-1] * arr[-2], arr[0] * arr[1], sep=' ')
