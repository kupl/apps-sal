# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        p = [int(x) for x in input().split()]
        q = [int(x) for x in input().split()]
        
        q[1] *= -1
        m = (q[1]-p[1])/(q[0]-p[0])
        c = p[1] - m*p[0]
        
        print("{:.2f}".format(-c/m))
except:
    pass
