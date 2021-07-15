
for _ in range(int(input())):
	q = []

	for __ in range(int(input())):
		a, b = list(input().split())
		b = int(b)
		q.append((a,b))

	q = sorted(q, key= lambda x:x[1])
	#print(q)
	i = 0
	win = ""
	if len(q) == 1:
		#print(q[0][0])
		continue
	while i < len(q):
		#print(i)
		t = q[i][1]

		if i == len(q)-1 or q[i][1] != q[i+1][1]:
			win = q[i][0]
			break

		while i < len(q) and q[i][1] == t:
			#print(q[i][1])
			i += 1
		#print(i)
		if i == len(q):
			break


	if win == "":
		print("Nobody wins.")
	else:
		print(win)












"""
2
5
Kouta 1
Yuka 1
Mayu 3
Lucy 2
Nana 5
2
Lucy 2
Nana 2

"""
