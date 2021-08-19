t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    wow = s
    for i in range(n):
        now = s[:i] + s[i + 1:]
        for j in range(n):
            wow = min(wow, now[:j] + s[i] + now[j:])

    print(wow)
'''    c=True
    ind=0
    while c and ind<n:
     m=min(s[ind:])
     if m==s[ind:][0]:
      ind+=1
      continue
     else:
      c=False
      if True:
       l=[j+ind for j,i in enumerate(s[ind:]) if i==m]
       #print([s[:ind]+s[aa]+s[ind:aa]+s[aa+1:] for aa in l])
       mm=min(l,key=lambda aa:s[:ind]+s[aa]+s[ind:aa]+s[aa+1:])
      s=s[:ind]+m+s[ind:mm]+s[mm+1:]
    print(s)'''
