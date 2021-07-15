for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    x = arr[int(input())-1]
    ans = 1
    for n in arr:
        if n < x: ans += 1
    print(ans)
