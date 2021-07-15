# cook your dish here
for _ in range(int(input())):
 n=input()
 count=0
 for j in range(0,len(n)-1):
  if n[j]!=n[j+1]:
   count+=1
   
 if n[0]!=n[-1]:
  count=count+1
 if count<=2:
  print("uniform")
 else:
  print("non-uniform")
