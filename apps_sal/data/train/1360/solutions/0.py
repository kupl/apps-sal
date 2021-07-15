for _ in range(eval(input())):
    S1=input()
    m1=len(S1)/2

    S2=input()
    m2=len(S2)/2
    d1={}
    d2={}
    for i in range(len(S1)):
        c=S1[i]
        v=abs(m1-i)
        if c in d1:
            if v<d1[c][0]:
                d1[c]=[v,i]
        else:
            d1[c]=[v,i]
    for i in range(len(S2)):
        c=S2[i]
        v=abs(m2-i)
        if c in d2:
            if v<d2[c][0]:
                d2[c]=[v,i]
        else:
            d2[c]=[v,i]

    mini=999999999999999999999999999999999
    for i in d1:
        if i in d2:
            L1=d1[i][1]
            L3=len(S1)-L1-1
            L2=d2[i][1]
            L4=len(S2)-L2-1
            v=abs(L1-L2)+abs(L2-L3)+abs(L3-L4)+abs(L4-L1)
            if v<mini:
                mini=v
    print(mini)
