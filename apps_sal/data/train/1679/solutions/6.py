# cook your dish here
t = int(input())

while(t > 0):
    t -= 1
    n, k, x = list(map(int, input().split()))
    while(n > 0):
        n -= 1
        print(x, end=' ')
        for i in range(k - 1):
            if(n > 0):
                print(0, end=' ')
                n -= 1
    print('\n')
