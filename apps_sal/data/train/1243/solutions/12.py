def f(n):
    string = str(n)
    for char in string:
        if char in '05':
            return 1
    return 0


t = int(input())
answers = list()
for _ in range(t):
    n = int(input())
    answers.append(f(n))

for answer in answers:
    print(answer)
