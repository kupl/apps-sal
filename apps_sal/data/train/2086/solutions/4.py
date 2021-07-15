# import sys
# input = sys.stdin.readline
n,queries = list(map(int,input().split()))
l = list(map(int,input().split()))
if(queries==0):
	return
maxval = max(l)
pairs = []
count = 0
f = l[0]
secix = 1
while(f!=maxval):
	# print(l)
	count+=1
	f = l[0]
	s = l[secix]
	pairs.append([f,s])
	f,s= max(f,s), min(f,s)
	l[0] = f
	l.append(s)
	secix+=1
# print(secix)
l = [l[0]]+l[secix:]
# print(l)
for i in range(n-1):
	pairs.append([maxval,l[1+i]])
# print(pairs)
for m in range(queries):
	q = int(input())
	if(q<=count):
		print(str(pairs[q-1][0]),str(pairs[q-1][1]))
	else:
		q-=(count+1)
		pos = count+(q%(n-1))
		print(str(pairs[pos][0]),str(pairs[pos][1]))
