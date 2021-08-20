from itertools import permutations
EVI = {8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888, 8888, 88888, 888888, 8888888}
for n in [8885, 8855, 8853, 88885, 88855, 88853, 88553, 888885, 888855, 888853, 888555, 888553, 885533]:
    for perm in permutations(str(n)):
        EVI.add(int(''.join(perm)))


def solve(a, b):
    return sum((a <= n < b for n in EVI))
