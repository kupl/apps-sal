from itertools import permutations;get_words=lambda d:sorted(["".join(i) for i in set(list(permutations("".join(["".join([k * i for k in j]) for i, j in d.items()]))))])
