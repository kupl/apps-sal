r=lambda n:next((p+r(n//p)for p in range(2,int(n**.5)+1)if n%p<1),n)
factor_sum=f=lambda n:(lambda s:s<n and f(s)or n)(r(n))
