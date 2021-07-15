from sys import stdin
input=stdin.readline
R=lambda:map(int,input().split())
I=lambda:int(input())
n=I();v=[1]*n
a=list(R());d={}
for i,j in enumerate(sorted(a)):d[j]=i
ans=[]
for i in a:
	p=d[i]
	if v[p]:
		ans+=[],
		while v[p]:
			ans[-1]+=p+1,
			v[p]=0
			p=d[a[p]]
print(len(ans))
for i in ans:
	print(len(i),*i)
