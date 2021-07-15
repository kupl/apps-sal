for q in range(int(input())):
    n=int(input())
    s=[None,None]
    s[0]=input()
    s[1]=input()
    poss="YES"
    r=0
    for i in range(n):
        if s[r][i] in '12':
            continue
        elif s[r^1][i] not in '12':
            r^=1
        else:
            poss="NO"
            break
    if r==0:
        poss="NO"
    print(poss)
