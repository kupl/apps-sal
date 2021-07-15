n = int(input())
questions = []
for i in range(2, n + 1):
	if all(i % q != 0 for q in questions):
		x = i
		while x <= n:
			questions.append(x)
			x *= i
print(len(questions))
print(' '.join(str(q) for q in questions))

