tops=lambda s:''.join(s[n*(2*n-1)]for n in range(int(((8*len(s)+1)**.5+1)/4),0,-1))
