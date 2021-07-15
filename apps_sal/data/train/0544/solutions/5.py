# cook your dish here
def find(n,i):
 if i=='0':
  return n//2
 else:
  return n
  
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
test=int(input())
while(test!=0):
 bits=int(input())
 li=list(input())
 k=0
 while(bits>=4):
  t=16
  s=''
  for i in range(k,k+4):
   s=s+li[i]
  bits=bits-4
  k=k+4
  s=int(s,2)
  print(alphabets[s],end="")
 print()
 test=test-1
