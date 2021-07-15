series = [0]
for a in range(2, 99):
    for b in range(2, 42):
        c = a**b
        if a == sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__
