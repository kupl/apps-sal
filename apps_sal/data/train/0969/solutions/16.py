'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP    , Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS,     SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''



t=int(input())
for i in range(t):
 count=0
 x, y =list(map(str,input().split(" ")))
 l=[]
 for i in range(int(x)):
  val=input()
  l.append(val)
 for i in l:
  i=i.split(" ")
  if(i[0]=="TOP_CONTRIBUTOR"):
   count=count+300
  if(i[0]=="CONTEST_HOSTED"):
   count=count+50
  if(i[0]=="CONTEST_WON"):
   if(int(i[1])<20):
    count=count+300+(20-int(i[1]))
   else:
    count=count+300
  if(i[0]=="BUG_FOUND"):
   count=count+int(i[1])
 if y=="INDIAN":
  print(count//200)
 else:
  print(count//400)
   

