for i in range(int(input())):
    a,b,c=[int(x) for x in input().split()]
    if a>0 and b>0 and c>0:
        if a**2+b**2==c**2:
            print("YES")
        elif b**2+c**2==a**2:
            print("YES")
        elif a**2+c**2==b**2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    

