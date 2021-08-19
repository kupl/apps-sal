# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans1, ans2, f = 0, 0, 21
    for i in range(n):
        if a[i] != 0:
            ans1 = i
            f = 7
            break
    for j in range(n - 1, -1, -1):
        if a[j] != 0:
            ans2 = n - j - 1
            f = 7
            break
    # print(ans1,ans2)
    if f != 7:
        print("1")
    else:
        print(n - (ans1 + ans2))
