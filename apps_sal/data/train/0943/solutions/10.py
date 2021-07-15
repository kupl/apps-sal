for _ in range(int(input())):
    v,w = map(int,input().split())
    if v is w :
        print(w+1)
    elif w>v:
        print(v+1)
    else:
        print(w+1)
