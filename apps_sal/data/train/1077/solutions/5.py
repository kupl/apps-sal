tc = int(input())
while tc:
	n = int(input())

	direction = []
	road = []

	for i in range(0,n):
		line = input()
		direction.append(line[0])

		if line[0] == 'B' or line[0] == 'R':
			road.append(line[9:])
		else:
			road.append(line[8:])

	print('Begin on ' + road[n-1])
	for i in range(0,n-1):
		if(direction[n-i-1] == 'R'):
			op = 'Left on '
		else:
			op = 'Right on '
		print(op + road[n-i-2])
	print()

	tc -= 1
