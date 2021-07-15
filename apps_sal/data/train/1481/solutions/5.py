t=int(input())
for i in range(1,t+1):
 st=input()
 a=st.count('0',0,len(st))
 b=st.count('1',0,len(st))
 if len(st)%2==1 or a==0 or b==0:
  ans=-1
 else:
  ans=abs(a-b)//2
 print(ans)

