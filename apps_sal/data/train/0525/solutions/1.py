try:
    for _ in range(int(input())):
        a,b,c=[int(i) for i in input().split()]
        r=c%a
        if(r>b):
            print(c-(r-b))
        elif(r<b):
            print(c-r-a+b)
        else:
            print(c)
except EOFError as e:
    pass
