for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sum1 = 0
    for x in arr:
        if (x % 2 == 0):
            sum1 += x
    print(sum1)
