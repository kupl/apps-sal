# cook your dish here
test=int(input())
dic={}
for _ in range(test):
 dic={}
 n=int(input())
 for i in range(n):
  a=input().split()
  l=[int(a[i]) for i in range(1,int(a[0])+1)]
  dic[i]=l
 c=0
 lg=[]
 for i in dic:
  c+=len(dic[i])
 chef={i:dic[i][0] for i in range(n)}
 ram={i:dic[i][len(dic[i])-1] for i in range(n)}
 #chef={k: v for k, v in sorted(chef.items(), key=lambda item: item[1])}
 #ram={k: v for k, v in sorted(ram.items(), key=lambda item: item[1])}
 i=0
 ans=0
 while(i<c):
  if(i%2==0):
   var=min(chef,key=chef.get)
   #print(chef[var])
   ans+=chef[var]
   if(len(dic[var])==1):
    chef.pop(var)
    ram.pop(var)
    dic[var].pop(0)
   else:
    dic[var].pop(0)
    chef[var]=dic[var][0]
   #print("dic=",dic)
  else:
   var=min(ram,key=ram.get)
   lg=len(dic[var])-1
   if(lg==0):
    chef.pop(var)
    ram.pop(var)
   else:
    dic[var].pop(lg)
    ram[var]=dic[var][lg-1]
   #print("dic=",dic)

  i+=1
 print(ans)
 
  
  

