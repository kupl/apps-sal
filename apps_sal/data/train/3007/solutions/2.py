def consecutive_sum(n):
    top = (1+(1+8*n)**.5) / 2
    return sum( not (n - (v-1)*v//2) % v for v in range(1,int(top)))
