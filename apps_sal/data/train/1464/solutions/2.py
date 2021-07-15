for _ in range(int(input())):
 EVEN=[4,6,9,11]
 ODD=[1,3,5,7,8,10,12]
 Y,M,D=list(map(int,input().strip().split(":")))
 Ans=0
 if Y%400==0 or (Y%4==0 and Y%100!=0):
  ODD.append(2)
  if M in EVEN:
   if D%2==0:
    Ans=(((30-D)//2)+1)+15
   else:
    Ans=(((30-D)//2)+1)+16
  elif M in ODD:
   if D%2==0:
    if M==2:
     Ans=(((29-D)//2)+1)
    else:
     Ans=(((31-D)//2)+1)
   else:
    if M==2:
     Ans=(((29-D)//2)+1)
    else:
     Ans=(((31-D)//2)+1)
 else:
  EVEN.append(2)
  if M in ODD:
   if D%2==0:
    Ans=(((31-D)//2)+1)
   else:
    Ans=(((31-D)//2)+1)
  elif M in EVEN:
   if D%2==0:
    if M==2:
     Ans=(((28-D)//2)+1)+15
    else:
     Ans=(((30-D)//2)+1)+15
   else:
    if M==2:
     Ans=(((28-D)//2)+1)+16
    else:
     Ans=(((30-D)//2)+1)+16
 print(Ans)
 
  

