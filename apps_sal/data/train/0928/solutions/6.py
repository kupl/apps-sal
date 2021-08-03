t = int(input())

for _ in range(t):

    n = int(input())

    '''
	a = [0] * n

	for i in range(n):

		for j in range(i, n, i+1):

			if (j+1) % 3 == 0:
				continue

			a[j] = 0 if a[j] else 1

	print(a)

	'''

    i = 2
    count = 1
    while 1:

        if i * i > n:
            break

        if i % 3 != 0:
            count += 1

        i += 1

    print(count)
