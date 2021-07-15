# cook your dish here
t=int(input())
for _ in range (t):
    x=input()
    t=0
    cnt=0
    lst=[]
    for i in x:
        if (i=='<'):
            lst.append(i)
        else:
            if len(lst)==0:
                break
            else:
                lst.pop()
                if len(lst)==0:
                    cnt+=2 + t
                    t = 0
                else:
                    t+=2
    print(cnt)
