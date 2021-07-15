k=str(input())
l=len(k)
paths=[]
for i in range(l):
	paths.append([1]*i+[int(k[i])]+[10]*(l-i-1))
lens = [sum(p) for p in paths]
n = sum(lens)+2
m = ['']*n
m[0] = 'N'*2
for i in range(len(paths)):
	m[0] += 'Y'*paths[i][0]+'N'*(lens[i]-paths[i][0])
m[1] = 'N'
for i in range(len(paths)):
	m[1] += 'N'*(lens[i]-paths[i][-1])+'Y'*paths[i][-1]
ind=2
for p in paths:
	for i in range(len(p)-1):
		for j in range(p[i]):
			m[ind] = 'N'*(p[i]-j)+'Y'*(p[i+1])+'N'*n
			ind+=1
	for j in range(p[-1]):
		m[ind] = 'N'*n
		ind+=1
m2=['']*n
for i in range(n):
	m2[i] = ''
	for j in range(i):
		m2[i]+=m2[j][i]
	m2[i]+=m[i][:n-i]
print(len(m2))
for s in m2:
	print(s)

