import sys
from collections import defaultdict as dd
input = sys.stdin.readline
I = lambda : list(map(int,input().split()))

n,a,b=I()
l=I()
dic=dd(int)
for i in range(n):
	dic[l[i]]=1
bs=[]
pa=dd(int)
for i in range(n):
	if dic[a-l[i]]==0:
		bs.append(l[i])
	else:
		pa[l[i]]=a-l[i]
j=0
while j<len(bs):		
	for i in range(j,len(bs)):
		cr=bs[i]
		dic[cr]=2
		if dic[b-cr]==0:
			print("NO");return
		dic[b-cr]=2
		if dic[a-b+cr]==1:
			dic[a-b+cr]=2
			bs.append(a-b+cr)
		j+=1
		#ct=0;vt=a-b+cr
		#while vt!=pa[pa[vt]]:
		#	vt=pa[vt];dic[b-vt]=2
		#	dic[vt]=2
an=[0]*n
for i in range(n):
	an[i]=dic[l[i]]-1
print("YES")
print(*an)

