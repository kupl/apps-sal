for i in range(int(input())):
    n = int(input())
    ans = 0
    while(n != 0):
        k = n // 10
        ans += k * 10
        n -= (k * 10)
        n += k
        if(k == 0):
            ans += n
            break
    print(ans)
