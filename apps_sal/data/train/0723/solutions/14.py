arr=[]
for II_II in range(eval(input())):
 n=eval(input())
 for KK_KK in range(n):
  cof,exp=list(map(int,input().split()))
  if exp==0:
   continue
  if (exp>1):
   arr.append(str(cof*exp)+"x^"+str(exp-1))
  if (exp==1):
   arr.append(str(cof*exp))
 #print arr
 str1 = ' + '.join(str(e) for e in arr)
 print(str1)
 #"+".join(l)
 arr[:]=[]
 
 

   
 

