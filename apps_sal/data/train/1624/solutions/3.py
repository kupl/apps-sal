r,p=lambda n:int(str(n)[::-1]),lambda n:pow(2,n,n)==2
sq_cub_rev_prime=([0]+[n for n in range(2,10**5)if p(r(n**2))*p(r(n**3))]).__getitem__
