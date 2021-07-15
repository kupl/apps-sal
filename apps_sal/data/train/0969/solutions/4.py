T=int(input())
for i in range(T):
 a,o=(input().split())
 a=int(a)
 l=0
 for j in range(a):
  s=(input().split())
  if s[0]=="CONTEST_WON":
   if int(s[1])<=20:
    l+=(300+(20-int(s[1])))
   else:
    l+=300
  if s[0]=="TOP_CONTRIBUTOR":
   l+=300
  if s[0]=="BUG_FOUND":
   if 50<=int(s[1])<=1000:
    l+=int(s[1])
  if s[0]=="CONTEST_HOSTED":
   l+=50
 if o=="INDIAN":
  print(l//200)
 elif o=="NON_INDIAN":
  print(l//400)
  

