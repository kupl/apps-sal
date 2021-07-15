try:
	for _ in range(int(input())):
		n=int(input())
		L=[*map(lambda i: str(i), range(n,0,-1))]
		print("".join(L))
		for i in range(len(L)-1):
			L[i]="*"
			print("".join(L))
except: pass
