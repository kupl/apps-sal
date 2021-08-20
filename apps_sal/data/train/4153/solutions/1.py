LIMIT = 2500000
RECA_SUM = [0, 0]
seen = {0}
last = 0
total = 0
for n in range(1, LIMIT):
    new = last - n
    if new < 0 or new in seen:
        new = last + n
    seen.add(new)
    total += new
    RECA_SUM.append(total)
    last = new
del seen


def rec(x):
    return RECA_SUM[x]
