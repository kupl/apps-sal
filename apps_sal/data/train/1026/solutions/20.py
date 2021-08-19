c = 10 ** 9 + 7
for i in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    ans = arr[0] * (arr[1] - 1) * (arr[2] - 2)
    print(ans % c)
