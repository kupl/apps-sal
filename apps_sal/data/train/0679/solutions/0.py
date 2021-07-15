t=eval(input())
 
a=[]
b=[]
 
top=-1
 
for __ in range(0,t):
 
 x=input().split()
 
 if(x[0]!="-1" and x[0]!="0"):
  
  add=int(x[0])
  
  if top!=-1 and add>a[top][0] :
    
    b[top]+=1
    
  else:
    a.append((add,x[1]))
    
    b.append(0)
    top+=1
  
  
 elif (x[0]=="-1"):
  
  #print("%s %s" %(b[top],a[top][1]))
  print((b[top]), end=' ')
  print(a[top][1])
  foo=a.pop()
  bar=b.pop()
  top-=1
