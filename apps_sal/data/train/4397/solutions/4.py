import itertools


def genThueMorse():
    for n in itertools.count():
        yield (1 if bin(n).count('1') % 2 else 0)


def is_thue_morse(seq):
    gen = genThueMorse()
    for i in range(len(seq)):
        if seq[i] != next(gen):
            return False

    return True
