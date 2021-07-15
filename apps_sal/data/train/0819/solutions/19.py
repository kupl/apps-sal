for _ in range(int(input())):
    x,y = map(int,input().split())
    Flag = False
    while x>=1 and y >= 1:    
        if x==1 or y==1:
            Flag = True
            break
        elif x==y and x!=1:
            break
        elif x > y:
            x = x - (x//y)*y
        else:
            y = y - (y//x)*x
    if Flag:
        print("YES")
    else:
        print("NO")
