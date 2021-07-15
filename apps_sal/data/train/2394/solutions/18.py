for nt in range(int(input())):
	n = int(input())
	s = input()
	stack = []
	ans = 0
	for i in range(n):
		if len(stack)==0:
			if s[i]==")":
				s += ")"
				ans += 1
			else:
				stack.append("(")
		else:
			if s[i]==")":
				stack.pop()
			else:
				stack.append("(")
	print (ans)
