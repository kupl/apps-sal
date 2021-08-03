def f(n):
    if n == 1:
        return print(1)

    p = 2
    print(1)

    line = 2
    while line < n:
        print(p, " " * (line - 2), p + 1, sep="")
        p += 2
        line += 1

    for i in range(n):
        print(p, end="")
        p += 1
    print()


t = int(input())
answers = list()
for _ in range(t):
    n = int(input())
    answers.append(n)

for answer in answers:
    f(answer)
