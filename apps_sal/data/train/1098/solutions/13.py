# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    for i in range(n - 1, -1, -2):
        count += arr[i]
    print(count)
