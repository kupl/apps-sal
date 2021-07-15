for t in range(int(input())):
    a,b,c,d=[int(x) for x in input().split()]
    if c==d and a!=b:
        print("NO")
    elif c==d and a==b:
        print("YES")
    elif abs(a-b)/abs(c-d)==abs(a-b)//abs(c-d):
        print("YES")
    else:
        print("NO")

