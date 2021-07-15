try:
    for i in range(int(input())):
        n=int(input())
        a=0
        b=1
        if n==1:
            print("0")
        elif n==2:
            print("1")
        else:
            
            print(((n-1)*(n)*((2*(n-1)+1)))//6)
except Exception :
    pass
