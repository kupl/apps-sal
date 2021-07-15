for i in range(int(input())):
    s,sg,fg,d,t = list(map(int,input().split()))
    tot = (50*d*3.6)/t
    final = s + tot
    a = abs(sg-final)
    b = abs(fg-final)
    if a<b:
        print("SEBI")
    elif a>b:
        print("FATHER")
    else:
        print("DRAW")
