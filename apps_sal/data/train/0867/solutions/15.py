for i in range(int(input())):
 count=0
 (strength,w1,w2,w3)=map(int,input().split())
 if w1+w2+w3<=strength:
  count=count+1
 elif w1+w2<=strength:
  count=count+2
 elif w1+w2>strength:
  if w2+w3<=strength:
   count=count+2
  elif w3<=strength:
   count=count+3
 elif w1<=strength:
  count=count+3
 print(count)
