def ds(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum

t = int(input())

for _ in range(t):
	n,d = input().split()
	n = int(n)
	d = int(d)

	s = set()
	temp = n
	for i in range(500000):
		if temp<=9:
			if not temp in s:
				s.add(temp)
				temp = temp+d
			else:
				break
		else:
			temp = ds(temp)

	s = sorted(s)
	k = s[0]

	q = []
	ans = 0 
	q.append((n,1))
	while len(q) != 0:
		num = q[0][0]
		step = q[0][1]
		q.pop(0)
		if num is k:
			ans = step-1
			break
		q.append((num+d,step+1))
		q.append((ds(num),step+1))
		
	print(str(k)+" "+str(ans))

