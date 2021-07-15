try:
    x=int(input())
    a=[*map(int, input().split())]
    b=[*map(int, input().split())]
    for i in b:
        y=a.count(i)-b.count(i)
        if y!=0:
            print(i)
            break
except: pass
