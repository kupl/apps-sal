from itertools import cycle
def interpreter(tape, array):
    output = ""
    for c in cycle(tape):
        if not array:
            return output
        if c == "0":
            output = output + array[0]
            array = array[1:]
        else:
            array = ("1" if array[0] == "0" else "0") + array[1:]
