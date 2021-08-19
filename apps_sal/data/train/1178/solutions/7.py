for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr = sorted(arr)
    for x in range(n):
        if arr[x] <= count:
            count += 1
        else:
            break
    print(count)
