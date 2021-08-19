def f(n):
    if n == 1:
        return print(0)
    print('0\n1 1')
    if n == 2:
        return
    fibo = [0, 1, 1]
    p = 3
    line = 3
    while line <= n:
        for _ in range(line):
            fibo.append(fibo[-1] + fibo[-2])
            print(fibo[-1], '', end='')
        print()
        line += 1


t = int(input())
answers = list()
for _ in range(t):
    n = int(input())
    answers.append(n)
for answer in answers:
    f(answer)
