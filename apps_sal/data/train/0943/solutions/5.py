def main():
	t=int(input())
	while t>0:
		v,w=map(int,input().split())
		i=v
		j=0
		count=0
		while i>=0 and j<=w:
			i-=1
			j+=1
			count+=1
		print(count)
		t-=1
main()
