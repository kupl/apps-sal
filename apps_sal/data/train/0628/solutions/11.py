t = int(input())
for i in range(t):
    s = input()
    if(s == "W"):
        print("Chef")
    elif(s == "WB" or s == "BW"):
        print("Aleksa")
    else:
        l = list(s)
        le = len(l)
        x = l.index("W")
        l1 = l[0:x]
        l2 = l[x + 1:le]
        le1 = len(l1)
        le2 = len(l2)
        if(le1 ^ le2 == 0):
            print("Chef")
        else:
            print("Aleksa")
