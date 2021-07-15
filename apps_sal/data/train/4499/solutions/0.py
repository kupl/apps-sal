e = [1, 2]
for n in range(1, 10 ** 4):
    for f in 1, 2 * n, 1:
        e.append(f * e[-1] + e[-2])
convergents_of_e = lambda n: sum(map(int, str(e[n])))
