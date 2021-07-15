try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        odd = 0
        if n&1:
            odd=1 
            n-=3
        arr = []
        for i in range(1,n+1,2):
            arr.append(i+1)
            arr.append(i)
        if odd:
            arr.append(n+2)
            arr.append(n+3)
            arr.append(n+1)
        for i in arr:
            print(i,end = ' ')
        print()
        
except:
    pass
                

