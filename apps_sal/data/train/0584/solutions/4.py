

N=int(input())
lst=[]
lt=[]
count=[]
for i in range(N):
    string=input()
    lst.append(string)
    

for num in lst:
  if num.startswith("1"):
    x=num.find("0")
    y=num.find('1',x)
    if y == -1:
       z=lt.append(len(num[x:]))
    else :
       z=lt.append(len(num[x:y]))
  if num.startswith("0"):
    z=lt.append(0)
for i in lt:
  print(i)
    
  
   
    

