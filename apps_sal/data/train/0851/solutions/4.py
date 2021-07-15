# cook your dish here
t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	print(2*(n*k-n+1)/k)
