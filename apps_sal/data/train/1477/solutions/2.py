def Min_str():
 n = int(input())
 s = input()
 temp = s[:]
 for i in range(n):
  s1 = [ord(x) for x in s]
  t = s1[i]
  del s1[i]
  j = 0
  while(j<n-1):
   if(s1[j]>t):
    s1[j:j]=[t]
    break
   j+=1
  if(len(s1)!=n):
   s1+=[t]
  T="".join([chr(x) for x in s1])
  if(T<temp):
   temp = T
 print(temp)
t= int(input())
for i in range(t):
 Min_str()
