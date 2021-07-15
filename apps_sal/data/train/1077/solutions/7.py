import sys

t=int(sys.stdin.readline());
while t>0:
	directions=[];
	n=int(sys.stdin.readline());
	for i in range(0,n):
		line=sys.stdin.readline();
		directions.append(line);
	x=directions[len(directions)-1].split()[2:]
	print("Begin on", end=' ')
	for item in x:
		print(item, end=' ')
	print()
		
	for i in range(len(directions)-2,-1,-1):
		first=directions[i+1].split()[0]
		x=directions[i].split()[2:]
		if first=="Left":
			first="Right"
		elif first=="Right":
			first="Left"
		print(first+" on", end=' ')
		for item in x:
			print(item, end=' ')
		print()
	if t!=1:	
		print()
	t -= 1;

