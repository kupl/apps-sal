# cook your dish here

T = int(input())
while(T):
    n = int(input())
    l = [int(k) for k in input().split()]
    c = 0
    for i in l:
        if(i % 2 == 0):
            c += i
    print(c)

    T -= 1
