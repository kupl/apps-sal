import sys
input=sys.stdin.readline
from bisect import bisect_left
n,q=map(int,input().split())
stop=[]
for i in range(n):
	s,t,x=map(int,input().split())
	stop.append((s,t,x))
stop.sort(key=lambda x:x[2])
d=[int(input())for i in range(q)]
R=[-1]*q
ans=[-1]*q
for s,t,x in stop:
	#lからrにある区間のansをxに更新したい
	l=bisect_left(d,s-x)
	r=bisect_left(d,t-x)
	while l<r:
		if R[l]==-1:#最左がまだ確定していない場合
			ans[l]=x
			R[l]=r
			l+=1
		else:
			l=R[l]#確定しているところを飛ばす
for x in ans:
	print(x)
