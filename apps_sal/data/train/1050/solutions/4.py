def compiler(string):
	t=0
	ans=0
	for i in range(len(string)):
		if string[i]=='<':
			t+=1
		else:
			t-=1
			if t==0:
				ans = max(ans, i+1)
			elif t<0:
				break
	return ans

t = int(input())
while t:
	string = input()
	print(compiler(string))
	t-=1

