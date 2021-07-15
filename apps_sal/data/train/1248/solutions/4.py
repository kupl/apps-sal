t = int(input())
for i in range(0, t):
    n = int(input())
    c = 1
    if n == 0:
        print(0)
    elif n == 1:
        print("INFINITY")
    else:
        for j in range(3, n+1):
            a = n
            while a >= j:
                a = int(a/j)
            if a == 1:
                c = c+1
        print(c)
        
