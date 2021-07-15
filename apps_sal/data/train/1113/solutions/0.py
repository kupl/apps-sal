t = input();

a = [0 for i in range(10001)]

i = 0;

while i < int(t):

	n = input();

	k = input();

	assert(len(k.split(' ')) == int(n));

	for each in k.split(' '):

		a[int(each)] += 1;


	V = 0;

	C = a[V];

	for j in range(10001):

		if C < a[j]:

			V = j;

			C = a[V];

		a[j] = 0;

	i += 1;

	print(V, C);

