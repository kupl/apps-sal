# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        p, q, r = list(map(int, input().split()))
        a, b, c = list(map(int, input().split()))
        
       
        if a<p or b<q or c<r:
            print(-1)
        else:
            print(a-p+b-q+c-r)
except EOFError:pass

