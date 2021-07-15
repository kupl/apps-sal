# cook your dish here

t = int(input())

for _ in range(t):
    s = ''
    n = int(input())
    if n==1:
        print(1)
        continue
    for i in range(1, n+1):
        s = s + str(i)
    print(s)
    
    p = 1
    for i in range(n-1):
        s = ''
        for j in range(n):
            s = s + str(p + n)
            p = p+1
            
        print(s)
        

