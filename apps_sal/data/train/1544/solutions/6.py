n = int(input())
while(n>0):
    n-=1
    a = int(input())
    print("*")
    for i in range(2,a):
        print("*", end='')
        print(" "*(i-2), end='')
        print("*")
    if(a!=1):
        print("*"*a)


