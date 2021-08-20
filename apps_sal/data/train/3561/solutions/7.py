import textwrap


def around_fib(n):
    fib = [0, 1]
    for i in range(n - 1):
        fib.append(fib[i] + fib[i + 1])
    cnt = [0] * 10
    for v in str(fib[-1]):
        cnt[int(v)] += 1
    chunk = textwrap.wrap(str(fib[-1]), 25)
    return 'Last chunk ' + chunk[-1] + '; Max is ' + str(max(cnt)) + ' for digit ' + str(cnt.index(max(cnt)))
