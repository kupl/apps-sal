(b_cnt, res) = (0, 0)
mod = 10 ** 9 + 7
for c in input()[::-1]:
    if c == 'b':
        b_cnt += 1
    else:
        res += b_cnt
        b_cnt *= 2
        res %= mod
        b_cnt %= mod
print(res)
