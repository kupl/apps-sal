# cook your dish here
for T in range(int(input())):
 n,ind = input().split()
 n = int(n)
 laddu = 0
 for i in range(n):
  ls = list(input().split())
  if len(ls)==2:
   if ls[0] == "CONTEST_WON":
    k = int(ls[1])
    if 20>=k:
     laddu = laddu+(300+(20-k))
     # print(laddu)
    else:
     laddu = 300 + laddu
   elif ls[0] == "BUG_FOUND":
    d = int(ls[1])
    laddu = laddu+d 
    # print(laddu)
  else:
   if ls[0]=="TOP_CONTRIBUTOR":
    laddu = laddu+300
   else:
    laddu = laddu+50
  
 if ind == "INDIAN":
  print(laddu//200)
 else:
  print(laddu//400)
 
# t=int(input())
# for z in range(t):
#   a=list(map(str,input().split()))
#   m=int(a[0])
#   s=a[1]
#   flag=0
#   if(s=="INDIAN"):
#     flag=1
#   ans=0
#   for i in range(m):
#     b=list(map(str,input().split()))
#     if(len(b)==2):
#       if(b[0]=="CONTEST_WON"):
#         val=int(b[1])
#         if(val>20):
#           ans+=300
#         else:
#           ans+=300+(20-val)
#       elif(b[0]=="BUG_FOUND"):
#         d=int(b[1])
#         ans+=d
#     else:
#       if(b[0]=="TOP_CONTRIBUTOR"):
#         ans+=300
#       else:
#         ans+=50
#   # print(ans)
#   sol=0
#   if(flag==1):
#     sol=ans//200
#   else:
#     sol=ans//400
#   print(sol)

