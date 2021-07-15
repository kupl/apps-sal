tests = int(input())
for t in range(tests):
  n = int(input())
  permut='2'
  if n%2==0:
    for i in range(2, n+1):
      if i%2==1:
        permut=permut+' '+str(i+1)
      else:
        permut=permut+' '+str(i-1)
    print(permut)
    pass
  elif n==1:
    print(1)
    pass
  else:
    for i in range(2, n):
      if i%2==1:
        permut=permut+' '+str(i+1)
      else:
        permut=permut+' '+str(i-1)
    edit_permut = permut[:-1]
    temp=permut[-1]
    edit_permut=edit_permut+str(n)
    edit_permut=edit_permut+' '+temp
    print(edit_permut)
    pass
