i = input('')
i = int(i)

x = 0
ans = []

while (x < i):
	a = input('')
	arr = input('')
	arr = arr.split()
	
	cnts = []
	y = 0
	
	while (y < len(arr)):
		temp = [0, 0]
		temp[0] = int(arr[y])
		temp[1] = arr.count(arr[y])
		cnts.append(temp)
		y = y + 1
		
	maxi = 10001
	maxicount = 0
	
	y = 0
	
	while (y < len(cnts)):
		if ((cnts[y])[1] > maxicount):
			maxicount = (cnts[y])[1]
			maxi = (cnts[y])[0]
		elif ((cnts[y])[1] == maxicount):
			maxicount = (cnts[y])[1]
			if ( (cnts[y])[0] < maxi ):
				maxi = (cnts[y])[0]
		y = y + 1
	
	ans.append(str(maxi) + ' ' + str(maxicount))
	
	x = x + 1
	
x = 0

while (x < len(ans)):
	print(ans[x])
	x = x + 1
