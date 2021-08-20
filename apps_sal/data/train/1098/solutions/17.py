for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    count = 0
    for i in range(0, len(arr), 2):
        count += arr[i]
    print(count)
