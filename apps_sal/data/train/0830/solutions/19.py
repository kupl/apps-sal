# cook your dish here
try:
 import string 
 alphabets=string.ascii_lowercase
 test=int(input())
 #ans=[]

 def solve():
  
  ans=[]
  n=int(input())
  string1=[]
  string2=[]
  present=[None]*26
  
  string1=list(input())
  string2=list(input())

  for i in range(n):
   if string1[i]<string2[i]:
    print(-1)
    return
  
  for i in range(n):
   present[ord(string1[i])-ord('a')]=1

  for i in range(n):
   if (present[ord(string2[i])-ord('a')]!=1):
    print(-1)
    return

  for alpha in alphabets[::-1]:
   index=[]
   
   for i in range(n):
    if(string1[i]!=alpha and string2[i]==alpha):
     index.append(i)

  
   if index:
    for i in range(n):
     if string1[i]==alpha:
      index.append(i)


   if index:
    ans.append(index)

   for i in range(len(index)):
    idx=index[i]
    string1[idx]=alpha 


  print(len(ans))
  for i in ans:
   i.sort()
   print(len(i),*i)
  #for i in ans:
   #print(" ".join(map(str,i)))

 for _ in range(test):
  solve()



 
except:
 pass
