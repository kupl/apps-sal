import sys

line = sys.stdin.readline()

t = int(line)

for i in range(0,t):
	line = sys.stdin.readline();
	n = int(line);
	r = []
	lr = []
	line = sys.stdin.readline();
	line = line.strip()
	#print("line " , line);
	r.append(line[9:])
	lr.append(-1)
	for j in range(1,n):
		line = sys.stdin.readline()
		line = line.strip()
		if (line[0:7] == "Left on"):
			lr.append(0)
			r.append(line[8:])
			#print(lr)
			#print(r)
		else:
			lr.append(1)
			r.append(line[9:])
			#print(lr)
			#print(r)
	print("Begin on " + r[n-1])
	j = n - 1;
	while j > 0:
		if (lr[j]):
			print("Left on " + r[j-1])
		else:
			print("Right on " + r[j-1])
		j = j - 1
	print("")

