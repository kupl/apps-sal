price=[]
for _ in range(int(input())):
 s=input().split()
 price.append(s[len(s)-1])
   
count=0
for i in price:
 e=i.count('8')
 f=i.count('5')
 t=i.count('3')
 d=i.count('.')
 if e+f+t+d==len(i):
  if e>=f and f>=t:
   count+=1
print(count)
