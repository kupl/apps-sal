# cook your dish here
for t in range(int(input())):
 s,w1,w2,w3=list(map(int,input().split()))
 if w1+w2+w3<=s:
  print('1')
 elif w1+w2<=s or w2+w3<=s:
  print('2')
 else:
  print('3')

