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
'    c=True\n    ind=0\n    while c and ind<n:\n     m=min(s[ind:])\n     if m==s[ind:][0]:\n      ind+=1\n      continue\n     else:\n      c=False\n      if True:\n       l=[j+ind for j,i in enumerate(s[ind:]) if i==m]\n       #print([s[:ind]+s[aa]+s[ind:aa]+s[aa+1:] for aa in l])\n       mm=min(l,key=lambda aa:s[:ind]+s[aa]+s[ind:aa]+s[aa+1:])\n      s=s[:ind]+m+s[ind:mm]+s[mm+1:]\n    print(s)'
