solve=lambda n:next((((n-x*x)//2//x)**2for x in range(int(n**.5),0,-1)if(n-x*x)%(2*x)==0<n-x*x),-1)
