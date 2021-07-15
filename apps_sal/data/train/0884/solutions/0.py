try:
    for _ in range(int(input())):
        s,s1=0,0
        x,k=[int(i) for i in input().split()]
        for i in range(2,x+1):
            if(x%i==0):
                s=s+i**k
        for i in range(2,k+1):
            if(k%i==0):
                s1+=i*x
        print(s,s1)
except EOFError as e:
    pass
