from functools import lru_cache as LC
FC = lambda n,li=[],j=2:(FC(n,li,j+1) if n%j else FC(n//j,li+[j],j)) if j*j<=n else sum(li+[[],[n]][n>1])
GF = LC(None)(lambda n:FC(n))
GD = LC(None)(lambda n:sum(sum([[i,n//i] for i in range(1,int(n**.5)+1) if not n%i],[])))
ds_multof_pfs = lambda start,end:[i for i in range(start,end+1) if not GD(i)%GF(i)]
