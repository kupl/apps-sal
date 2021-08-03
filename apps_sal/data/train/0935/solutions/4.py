t = int(input())
for ss in range(t):
    n = int(input())
    c = 0
    if(n % 10 == 0):
        c = 1
        print(0)
    elif(n % 10 != 0):
        for i in range(1, 11):
            if((n * (2**i)) % 10 == 0):
                c = 1
                print(i)
                break
    if(c == 0):
        print(-1)
