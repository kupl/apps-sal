for z in range(int(input())):
    s = input()
    n = len(s)
    i = 0
    while i<n and s[i]=='1':
        i+=1
    if i==0:
        print(0)
    else:
        k = 0
        while i<n and s[i]=='0':
            i+=1
            k+=1
        print(k)

