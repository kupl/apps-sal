for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.reverse()
    ans = n - 1
    flag = False
    for i in range(1, n):
        if ar[i] < ar[i - 1]:
            flag = True
        if flag:
            if ar[i] > ar[i - 1]:
                break
        ans -= 1
    print(ans)
