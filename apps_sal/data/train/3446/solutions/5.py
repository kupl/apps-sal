approx_root=r=lambda n,i=0:n>(i+1)**2and r(n,i+1)or round(i+(n-i*i)/(2*i+1),2)
