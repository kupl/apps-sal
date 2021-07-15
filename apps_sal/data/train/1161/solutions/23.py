t=int(input())
for i in range(t):
 s=input()
 list1=list(s)
 n=0
 n=len(s)
 c=0
 if(n==1):
  if(s[0]=="m"):
   print("mongooses")
  if(s[0]=="s"):
   print("snakes")
 elif(n==2):
  if(s!="ss"):
   print("mongooses")
  elif(s=="ss"):
   print("snakes")
   
 
 else:
  if(list1[0]=="m" and list1[1]=="s"):
   list1[1]=0
   c+=1
  for i in range(1,len(s)-1):
   if(list1[i]=="m" and list1[i-1]=="s"):
    c+=1
    list1[i-1]=0
   elif(list1[i]=="m" and list1[i+1]=="s"):
    c+=1
    list1[i+1]=0
   else:
    pass
  if(list1[n-1]=="m" and list1[n-2]=="s"):
   c+=1
   list1[n-2]=0
  if(s.count("m")>s.count("s")-c):
   print("mongooses")
  if(s.count("m")==s.count("s")-c):
   print("tie")
  if(s.count("m")<s.count("s")-c):
   print("snakes")
  
   

