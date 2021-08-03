from collections import defaultdict
from itertools import cycle

valid = ('<', '>', '+', '-', '*', '/', '\\', '&')


def interpreter(tape):
    memory = defaultdict(int)
    pointer = 0
    input = cycle(c for c in tape if c in valid)
    output = ''

    while True:
        c = next(input)
        if c == '>':
            pointer += 1
        elif c == '<':
            pointer -= 1
        elif c == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif c == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif c == '*':
            output += chr(memory[pointer])
        elif c == '/' and not memory[pointer]:
            next(input)
        elif c == '\\' and memory[pointer]:
            next(input)
        elif c == '&':
            return output
