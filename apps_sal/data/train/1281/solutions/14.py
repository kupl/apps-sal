# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 if 7 not in l:
  print('no')
  continue
 s=l.index(7)
 k=list(set(l[:s+1]))
 t=[i for i in range(1,8)]
 if k==t and l==l[::-1]:
  print('yes')
 else:
  print('no')
