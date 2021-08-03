for _ in range(int(input())):
    n = int(input())
    arr = input()
    ans = 0

    print(arr.count("1") * arr.count("0"))
    # for i in range(0, n-1):
    #     if arr[i] == "1":
    #         ans += arr[i+1:].count("0")
    #     else:
    #         ans += arr[i+1:].count("1")
    # print(ans)
