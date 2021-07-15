factors=lambda n:-1if not n or type(n)!=int or n<1else[e for e in range(n,0,-1)if n%e==0]
