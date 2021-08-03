from math import factorial


def rle(s):
    if not s:
        return []
    last = s[0]
    count = 0
    for curr in s:
        if last == curr:
            count += 1
        else:
            yield (last, count)
            count = 1
            last = curr
    else:
        yield (last, count)


def algo(n):
    ans = 0
    for repl_length in range(0, n + 1, 2):
        n_fs = n - repl_length
        n_cs = repl_length >> 1
        ans += factorial(n_fs + n_cs) // (factorial(n_fs) * factorial(n_cs))
    return ans


s = input()
ans = 1
for (char, count) in rle(s):
    if char in 'gf':
        ans *= algo(count)
print(ans)
