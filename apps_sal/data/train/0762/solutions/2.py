def f(n):
    p = 1
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print((str(bin(p))[2:])[::-1], "", end="")
            p += 1
            j += 1
        print()
        i += 1


t = int(input())
answers = list()
for _ in range(t):
    n = int(input())
    answers.append(n)

for answer in answers:
    f(answer)
