import itertools

def powerset(f,n):
	lst = []
	for i in range(1,n+1):
		lst.append(list(itertools.combinations(f,i)))
	return lst

def read():
	return input()

def add(s,f):
	result = ''
	# print 'adding '+s+' and '+f+' results in ',
	for i in range(len(s)):
		if s[i]=='+' and f[i]=='+':
			result+='-'
		elif s[i]=='+' or f[i]=='+':
			result+='+'
		else:
			result+='-'
	# print result
	return result

def resultfilter(f):
	result = f[0]
	if len(f)==1:
		return result
	for item in f[1:]:
		result = add(result,item)
	return result

def getRequired(s):
	f = ''
	for i in range(len(s)):
		if s[i]=='b':
			f+='-'
		else:
			f+='+'
	return f

for t in range(int(read())):
	s = read()
	if 'w' in s:
		count = 0
	else:
		count = 1
	requiredF = getRequired(s)
	# print 'required '+requiredF
	n = int(read())
	f = []
	for i in range(n):
		f.append(read())
	y = powerset(f,n)
	for item in y:
		for temp in item:
			# print temp
			output = resultfilter(temp)
			# print output
			# print output==requiredF
			if output == requiredF:
				# print 'Increasing count'
				count+=1
	print(count%1000000007)
