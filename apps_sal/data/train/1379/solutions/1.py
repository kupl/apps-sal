def remove_double(s):
 s.reverse()
 temp=list(set(s))
 for i in temp:
  t=s.count(i)
  for _ in range(t-1):
   s.remove(i)
 s.reverse() 
 return s

message=input().strip().lower()

alpha=remove_double(list(message))

l=len(alpha)

encrypted=''

for i in range(l):
 times=message.count(alpha[i])
 encrypted+=alpha[i]+str(times)
 
print(encrypted)
