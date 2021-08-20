RECA = [0]
seen = {0}
last = 0
for n in range(1, 30000):
    new = last - n
    if new <= 0 or new in seen:
        new = last + n
    RECA.append(new)
    seen.add(new)
    last = new
del seen


def recaman(n):
    return RECA[n]
