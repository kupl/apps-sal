t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    sm=1
    total=0
    for j in range(1,l):
        if s[j-1]==s[j]:
            sm+=1
        else:
            if sm==1:
                total+=8
            else:
                total+=8
                total=total+32
            sm=1
    if s[j-1]==s[j]:
            sm+=1
            total+=8
            total=total+32
    else:
        if sm==1:
            total+=8
        else:
            total+=8
            total=total+32
    print(l*8-total)
