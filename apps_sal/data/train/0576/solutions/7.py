# def count(a, b): 
# 	m = len(a);n = 1
# 	lookup = [[0] * (n + 1) for i in range(m + 1)] 
# 	for i in range(n+1): lookup[0][i] = 0
# 	for i in range(m + 1): lookup[i][0] = 1
# 	for i in range(1, m + 1): 
# 		for j in range(1, n + 1): 
# 			if a[i - 1] == b[j - 1]: lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
# 			else: lookup[i][j] = lookup[i - 1][j] 
# 	return lookup[m][n]
# for _ in range(int(input())):
# 	a = input()
# 	b = "a"
# 	print(count(a, b)) #this just counts the number of times a string occurs, nut the subsequences
#>>> if there are only a's, then answer is (2**len) - 1
#>>> if there are len - 1 a's and one diff, then answer is (2**len) - 2
#>>> if there are len - 1 diff's and one a, then answer is 2**(len - 1)
#>>> if there are all diff, then answer is 0
#>>> there has to be a direct relation somewhere...gottit..if there are equal a's and diffs, then answer is 2**len - 2**(len/2)
#>>> wait a minute...2**len - 2**(len/2) this works for inequalities also (?)
for _ in range(int(input())):
	a = input();count = 0
	for i in a:
		if(i != "a"): count += 1
	print(2**len(a) - 2**count)
