# cook your dish here
try:
 def convert(list): 
  s = [str(i) for i in list] 
  res = int("".join(s)) 
  return(res) 
 for _ in range(int(input())):
  x=int(input())
  while x>0:
   a=str(x)
   b=list(a)
   b.sort()
   if b==list(a):
    break
   else:
    k=0
    for j in b:
     if str(j)==a[k]:
      k+=1
     else:
      break
    k=convert(list(a[k+1:])) 
    x=x-k-1
  print(x)
except:
 pass
