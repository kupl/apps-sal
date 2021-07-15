x = list(map(int, input().split()))

n   = x[0]
x = x[1:]
a = {(i):x[i] for i in range(n)}
p = {(i):x[n+i] for i in range(n)}
#vis = [0]*n
#print(a,p)
#vis[p.index(-1)] = 2

bhutiya = []

for i in range(n):
	if p[i] != -1:
		#vis[i] = 1
		#rem = []
		#rem.append(a[i])
		j = p[i]-1
		maxi = a[i]
		#print("j:",j)
		while p[j] != -1:
			if a[j] > maxi:	maxi = a[j]
			#rem.append(a[j])
			#vis[j] = 1
			j = p[j]-1
		
		if a[j] > maxi:	maxi = a[j]
		
		bhutiya.append(maxi-a[i])

print(max(bhutiya))



