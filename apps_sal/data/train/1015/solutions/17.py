try:
    tc=int(input())
    for _ in range(tc):
        n=int(input())
        a=2
        for i in range(n):
            for j in range(n):
                print(a,end='')
                a+=2
            print()
except:
    pass
