for i in range(int(input())):
    n=input().split()
    if len(n)==1:
        t=n[0]
        print(t.capitalize())
    else:
        for i in n:
            if i!=n[-1]:
                t=i.capitalize()
                print(t[0],'.',sep='',end=' ')
            else:
                print(i.capitalize())
