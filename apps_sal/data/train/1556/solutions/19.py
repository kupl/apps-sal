for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("1")
    else:
        s=''
        for i in range(n):
            if i%2==0:
                s+='1'
            else:
                s+='0'
        for i in range(n):
            print(s)
