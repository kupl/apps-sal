for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    for i in range(n):
        if arr[i] <= count:
            count += 1
        else:
            break
    print(count)
