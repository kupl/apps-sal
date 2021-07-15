# your code goes here
for _ in range(int(input())):
 N,X=map(int,input().split())
 P,S=map(str,input().split())
 if P=='L':
  if X%2!=0:
   print('{} {}'.format(X,S))
  else:
   if S=='H':
    print('{} E'.format(X))
   else:
    print('{} H'.format(X))
 else:
  X=(N-X)+1
  if X%2!=0:
   print('{} {}'.format(X,S))
  else:
   if S=='H':
    print('{} E'.format(X))
   else:
    print('{} H'.format(X))
