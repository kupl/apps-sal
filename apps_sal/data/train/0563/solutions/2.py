for _ in range(int(input())):
    n = int(input())
    arr = [int(k) for k in input().split()]
    q = int(input())
    sum = 0
    for i in range(q):
        start,end = [int(k) for k in input().split()]
        for j in range(start - 1, end):
            sum = sum + arr[j]
        print(sum)
        sum = 0

