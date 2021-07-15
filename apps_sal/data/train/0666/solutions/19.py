try:
    tc=int(input())
    for _ in range(tc):
        n=int(input())
        a=1
        for i in range(n):
            for j in range(n):
                print(a,end='')
                a+=1
            print()
except:
    pass
