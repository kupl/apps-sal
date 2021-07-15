approx_root=lambda n:round(next(i+(n-i*i)/(2*i+1)for i in range(n)if(i+1)**2>=n),2)
