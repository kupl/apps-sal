for __ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    i = 0
    c = 0
    while(True):
        if arr[i] > k:
            ans = -1
            break
        else:
            w = 0
            flag = 0
            for j in range(i, n):
                if(w + arr[j] <= k):
                    w += arr[j]
                    flag = 1
                    i = j + 1
                else:
                    i = j
                    break
            if(flag == 1):
                c += 1
                ans = c
            if(i >= n):
                break

    print(ans)
