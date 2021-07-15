t = int(input())
while t:
 t-=1
 r,g,b,k,ans,cnt=0,0,0,0,0,0;
 r,g,b= input().split()
 r,g,b= int(r),int(g),int(b)
 k = int(input())
 if(r<k): ans+=r;
 else: cnt+=1;
 if(g<k): ans+=g;
 else: cnt+=1;
 if(b<k): ans+=b;
 else: cnt+=1;
 ans += cnt*(k-1) +1;
 print(ans)
 
 

