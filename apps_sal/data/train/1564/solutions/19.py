for i in range(int(input())):
  s=input()
  l=[]
  for j in range(len(s)-1):
    l.append(s[j:j+2])
  print(len(set(l)))
