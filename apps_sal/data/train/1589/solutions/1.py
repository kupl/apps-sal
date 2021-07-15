for i in range(int(input())):
    c = 0
    arr = list(map(int,input().split()))
    for k in arr:
        if k==-1:
            break
            arr.append(a)
        if k >30:
            c=c+1
    num = 0
    den = 0
    for i in range(0,len(arr)):
        if arr[i]%2==0:
            num = num + arr[i]*(i+1)
            den = den + i + 1
    print(c, "{:.2f}".format(num/den))
        
    
    

