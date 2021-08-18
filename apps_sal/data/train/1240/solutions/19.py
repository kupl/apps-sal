for t in range(int(input())):

    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for i in range(len(arr)):

        if arr[i] % 6 == 0:
            ans += 6

        else:
            ans += arr[i] % 6

    print(ans)
