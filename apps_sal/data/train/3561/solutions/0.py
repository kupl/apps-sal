from collections import Counter
fib = [0, 1]


def around_fib(n):
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    f = str(fib[n])
    val = max((v, -int(k)) for k, v in Counter(f).items())
    last = f[-(len(f) % 25 or 25):]
    return f"Last chunk {last}; Max is {val[0]} for digit {-val[1]}"
