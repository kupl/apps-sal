'''input
3 2
1 2 1
3 4
'''
n, m = [int(x) for x in input().split()]

pir = [int(x) for x in input().split()]
ant = [int(x) for x in input().split()]

ats = sum(pir)*m

did = max(pir)

antmaz = min(ant)

if antmaz < did:
	print(-1)
	return

pir.sort(reverse=True)
ant.sort()

for i in range(1, m):
	ats += ant[i] - did

if ant[0] != did:
	ats += ant[0] - pir[1]

print(ats)

