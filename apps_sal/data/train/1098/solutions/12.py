for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    for i in range(n - 1, -1, -2):
        count += arr[i]
    print(count)
