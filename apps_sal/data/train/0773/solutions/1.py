tests = int(input())
for t in range(tests):
  n = int(input())
  permut='2'
  permut_list=[]
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
        permut_list.append(str(i+1))
      else:
        permut_list.append(str(i-1))
    permut_list.pop(-1)
    permut_list.append(str(n))
    permut_list.append(str(n-2))
    this_permut='2'
    for el in permut_list:
      this_permut=this_permut+' '+el
    print(this_permut)
