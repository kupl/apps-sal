def fusc(n):
   r=0; s=1
   while n>0:
     if (n&1)==0:n>>=1; s+=r; continue
     n=(n-1)>>1; r+=s
   return r
