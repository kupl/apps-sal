for _ in range(int(input())):
    n = int(input())
    n1 = 0
    ans = 1
    while(n > 0):
        d = int(n % 10)
        if(d != 0):
            if(d != 9 and d != 7 and d != 1):
                n1 = 3
            elif(d == 1):
                n1 = 1
            else:
                n1 = 4
            ans = (int(ans) * int(n1)) % (1000000007)
            n /= 10
        else:
            n /= 10
    if(ans == 1):
        print("0")
    else:
        print(ans % (1000000007))
