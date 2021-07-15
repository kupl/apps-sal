for _ in range(int(input())):
    s=input()
    n=len(s)
    c=s.count('a')
    l=n-c
    print(pow(2,n)-pow(2,l))


