def fibs_fizz_buzz(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(sum(fib[-2:]))
    fib = fib[:n]
    fib[3::4] = ['Fizz'] * (n // 4)
    fib[4::5] = ['Buzz'] * (n // 5)
    fib[19::20] = ['FizzBuzz'] * (n // 20)
    return fib
