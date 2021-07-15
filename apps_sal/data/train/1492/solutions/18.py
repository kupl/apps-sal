for x in range(0,int(input())):
 k,q=int(input()),100000
 for y in range(0,k):
  s=input()
  q=min(min(s.count('a'),s.count('b')),q)
 print(q)
