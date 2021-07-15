subfactorial = [1, 0]
for n in range(1, 10 ** 4):
    subfactorial.append(n * (subfactorial[-1] + subfactorial[-2]))
all_permuted = subfactorial.__getitem__
