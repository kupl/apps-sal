def abundant(h):
    for n in range(h,0,-1):
        s = sum(i for i in range(1,n//2+1) if not n%i)
        if s > n:
            return [[n],[s-n]]
