try:
    for _ in range(int(input())):
        s=input()
        l=len(s)
        k=8*l
        p=8
        t=0
        for i in range(1,l):
            if(s[i]==s[i-1]):
                if(t==0):
                    p+=32
                    t=1
            else:
                p+=8
                t=0
        print(k-p)
except EOFError as e:
    pass
