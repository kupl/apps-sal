n=int(input())

d={}; D={}; ans=[]

for _ in range(n): s=input()+'/'; t=s.find('/',7); d.setdefault(s[:t],set()).add(s[t:])

for k in d: D.setdefault(frozenset(d[k]),[]).append(k)

{ans.append(D[k]) for k in D if len(D[k])>1}

print(len(ans))

print('\n'.join(map(' '.join,ans)))



# Made By Mostafa_Khaled

