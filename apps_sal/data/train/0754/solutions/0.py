for i in range(int(input())):
    n = int(input())
    flag = 0
    while(n > 0):
        if((n % 10) % 2 == 0):
            flag = 1
            break
        n = n // 10
    if(flag == 0):
        print(0)
    else:
        print(1)
