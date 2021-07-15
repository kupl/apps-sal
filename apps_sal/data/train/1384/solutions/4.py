def pizzatime(s,a,k):
 cont1,m_time=0,0
 for i in range(len(s)):
  if(s[i]=='1'):
   cont1+=1
  else:
   try:
    m_time=max(m_time,cont1+k+a[i+k])
   except:
    m_time=max(m_time,cont1+min(k,len(s)-i))
   cont1=0
 m_time=max(m_time,cont1)
 return m_time
   
  
for T in range(int(input())):
 n,k=list(map(int,input().split()))
 s=input()

 all_1=[0]*(n+1)
 check=True
 for ind in range(len(s)-1,-1,-1):
  if(s[ind]=='1'):
   all_1[ind]+=(all_1[ind+1]+1)
   
 print(pizzatime(s,all_1,k))

