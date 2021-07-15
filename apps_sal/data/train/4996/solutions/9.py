def fib(n):
    f = [1,1]
    while len(f) < n:
        f.append(f[-2]+f[-1])
    return f[:n]


def fizz_buzzify(l):
    return ["Fizz"*(n%3==0)+"Buzz"*(n%5==0) or n for n in l]


def fibs_fizz_buzz(n):
    return fizz_buzzify(fib(n))

