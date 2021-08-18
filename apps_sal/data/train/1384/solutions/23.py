for z in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    maxl = 0
    for i in range(0, n - k + 1):
        j = i - 1
        c0 = 0
        c1 = 0
        while(j >= 0):
            if(s[j] == '1'):
                c0 += 1
                j -= 1
            else:
                break
        j = i + k
        while(j < n):
            if(s[j] == '1'):
                c1 += 1
                j += 1
            else:
                break
        if(maxl < (c0 + c1 + k)):
            maxl = c0 + c1 + k

    else:
        print(maxl)
