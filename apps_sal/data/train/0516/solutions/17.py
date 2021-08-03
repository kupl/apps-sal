# cook your dish here
t = int(input())
while(t):
    t -= 1
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = [0] * n
    ans2 = [0] * n
    for i in range(n):
        for j in range(n):
            if(i < j and arr[i] > arr[j]):
                ans[i] = ans[i] + 1
            if(i > j and arr[i] > arr[j]):
                ans2[i] = ans2[i] + 1
    # print(ans)
    # print(ans2)
    for i in range(n):
        if(ans[i] != 0):
            ans[i] = (ans[i] * k * (k + 1)) // 2
        if(ans2[i] != 0):
            ans2[i] = (ans2[i] * k * (k - 1)) // 2
    print(sum(ans) + sum(ans2))
