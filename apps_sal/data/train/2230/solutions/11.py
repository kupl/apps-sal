n = int (input ())

p = [int (i) for i in input().split()]

a = [int (i) for i in input().split()]

b = [int (i) for i in input().split()]


m = int (input())
c = [int (i) for i in input().split()]

c1 = {}
c2 = {}
c3 = {}

for i in range (n):
	if a[i] == 1 or b[i] == 1:
		c1[p[i]] = 1
	if a[i] == 2 or b[i] == 2:
		c2 [p[i]] = 1
	if a[i] == 3 or b[i] == 3:
		c3 [p[i]] = 1

k1 = sorted (c1)
k2 = sorted (c2)
k3 = sorted (c3)

k1s = 0
k2s = 0
k3s = 0

for i in range (m):
	ch = 0
	if c[i] == 1:
		for j in range (k1s, len (k1)):
			if c1 [k1[j]] != 0:
				c1 [k1[j]] = 0
				c2 [k1[j]] = 0
				c3 [k1[j]] = 0
				ch = 1
				k1s = j + 1
				print (k1[j], end = ' ')
				break
	else:
		if c[i] == 2:
			for j in range (k2s, len (k2)):
				if c2 [k2[j]] != 0:
					c1 [k2[j]] = 0
					c2 [k2[j]] = 0
					c3 [k2[j]] = 0
					ch = 1
					k2s = j + 1
					print (k2[j], end = ' ')
					break
		else:
			if c[i] == 3:
				for j in range (k3s, len (k3)):
					if c3 [k3[j]] != 0:
						c1 [k3[j]] = 0
						c2 [k3[j]] = 0
						c3 [k3[j]] = 0
						ch = 1
						k3s = j + 1	
						print (k3[j], end = ' ')
						break
	if ch == 0:
		print (-1, end = ' ')
