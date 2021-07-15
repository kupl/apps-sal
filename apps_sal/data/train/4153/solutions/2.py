s, seq, sums = {0}, [0], [0]
for i in range(25 * 10 ** 5 + 1):
    x = seq[-1] - i
    if x < 0 or x in s: x += 2 * i
    s.add(x); seq.append(x); sums.append(x + sums[-1])
rec=sums.__getitem__
