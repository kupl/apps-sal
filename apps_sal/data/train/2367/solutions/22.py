from string import ascii_lowercase

q = int(input())

for _ in range(q):
	n = int(input())
	A = input()
	B = input()

	c_a = {}
	c_b = {}

	ans = False

	if sorted(A) == sorted(B):
		inv_a = 0
		inv_b = 0
		has_multi = False

		for a in A:
			for k in c_a:
				if k > a:
					inv_a += c_a[k]

			if a not in c_a:
				c_a[a] = 0

			c_a[a] += 1

		for b in B:
			for k in c_b:
				if k > b:
					inv_b += c_b[k]

			if b not in c_b:
				c_b[b] = 0

			c_b[b] += 1

		for val in list(c_a.values()):
			has_multi = has_multi or (val > 1)

		if inv_a % 2 == inv_b % 2:
			ans = True

		elif has_multi:
			ans = True

	if ans:
		print("YES")
	else:
		print("NO")

