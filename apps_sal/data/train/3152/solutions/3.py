from itertools import cycle


def interpreter(tape, array):
    tape, array = cycle(tape), list(array)
    for i in range(len(array)):
        while next(tape) == "1":
            array[i] = "10"[int(array[i])]
    return "".join(array)
