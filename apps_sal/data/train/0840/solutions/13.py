def f(n):
    k = (n + 1) // 2

    def line(i):
        return print(' ' * (i - 1) + '*')
    for i in range(1, k + 1):
        line(i)
    i = k - 1
    while i > 0:
        line(i)
        i -= 1


t = int(input())
questions = list()
for _ in range(t):
    n = int(input())
    questions.append(n)
for question in questions:
    f(question)
