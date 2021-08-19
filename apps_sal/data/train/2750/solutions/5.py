D = [1, 2]
for _ in '_' * 1000:
    D += [D[-1] + D[len(D) // 2]]


def make_sequences(n):
    return D[n // 2]
