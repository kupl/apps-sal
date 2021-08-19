t = int(input())
while t > 0:
    n = int(input())
    if n == 1:
        print('0')
        t -= 1
        continue
    num = n * (n + 1) // 2
    fib = [0 for i in range(num)]
    fib[0] = 0
    fib[1] = 1
    for i in range(2, num):
        fib[i] = fib[i - 1] + fib[i - 2]
    cnt = 0
    for i in range(n):
        for j in range(i + 1):
            print(fib[cnt], end=' ')
            cnt += 1
        print()
    t -= 1
