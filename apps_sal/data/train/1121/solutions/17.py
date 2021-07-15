# cook your dish here
t=int(input())
while t:
 t=t-1
 s=input()
 hrs=""
 mint=""
 for i in range(len(s)):
  if(s[i]!=":"):
   hrs+=s[i]
  else:
   mint=s[i+1:]
   break
 mint=int(mint)
 hrs=int(hrs)
 if mint%5!=0:
  mint+=(5-(mint%5))
 if hrs>=12:
  hrs-=12
 if mint==60:
  mint=0
 h_hand=30*hrs+(float)((float)(2.5)*(float)(mint/5))
 m_hand=30*(mint/5)
 hour=abs(h_hand-m_hand)
 if abs(h_hand-m_hand)==int(abs(h_hand-m_hand)):
  hour=int(abs(h_hand-m_hand))
 min1=min(360-hour,hour)
 print(min1,"degree") 

