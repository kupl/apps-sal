# cook your dish here
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = arr[0]
    i = 0
    while(i < n - 1):
        ans = min(ans, arr[i] - arr[i + 1])
        i += 1
    print(ans)
