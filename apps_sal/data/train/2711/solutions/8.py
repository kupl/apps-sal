outcome=o=lambda n,s,k:s>=k>0if n==1else sum(o(n-1,s,k-i-1)for i in range(min(s,k)))
