s = input()
N = len(s)
flag = False
for i in range(N):
  if s[i]=='1':
    if s[N-2-i]!='1':
      print(-1)
      break
else:
  if s[0]=='0' or s[-1]=='1':
    print(-1)
  else:
    s = list(s)
    s[-1] = '1'
    ls = []
    for i in range(N):
      if s[i]=='1':
        ls.append(i)
    ps = 0
    for i in range(N-1):
      if i==ls[ps]:
        ps += 1
      print(i+1,ls[ps]+1)
