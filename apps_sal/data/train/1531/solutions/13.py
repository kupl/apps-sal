# cook your dish here
while True:
    try:
        n=int(input())
        lst=[int(i) for i in input().split()]
        for _ in range(int(input())):
            a,b=[int(i) for i in input().split()]
            a=a-1
            if (a-1)>=0:
                lst[a-1]+=b-1
            if (a+1)<n:
                lst[a+1]+=lst[a]-b
            lst[a]=0
        for i in lst:
            print(i)
    except:
        break

