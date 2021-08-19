from random import choice

DIR = (1, 0), (-1, 0), (0, 1), (0, -1)


def interpret(code):
    grid, stack, out, direction = [*map(list, code.splitlines())], [], '', DIR[0]
    x = y = smode = value = 0
    while True:
        value, jump = grid[y][x], 1
        if value is '"':
            smode = not smode
        elif smode or value.isdigit():
            stack += [(int, ord)[smode](value)]
        elif value in '+-*/%':
            stack += [eval(str(stack.pop(~1)) + value + str(stack.pop()))]
        elif value in '!':
            stack += [not stack.pop()]
        elif value in '`':
            stack += [stack.pop() < stack.pop()]
        elif value in ':':
            stack += [stack and stack[-1] or 0]
        elif value in '\\':
            stack += [len(stack) > 1 and stack.pop(-2) or 0]
        elif value in 'g':
            stack += [ord(grid[stack.pop()][stack.pop()])]
        elif value in 'p':
            grid[stack.pop()][stack.pop()] = chr(stack.pop(-3))
        elif value in '$':
            stack.pop()
        elif value in '.,':
            out += (str, chr)[value is ','](+stack.pop())
        elif value in '?':
            direction = choice(DIR)
        elif value in '_|':
            direction = DIR[(value is '|') * 2 + bool(stack.pop())]
        elif value in '><v^':
            direction = DIR['><v^'.index(value)]
        elif value in '#':
            jump = 2
        elif value in '@':
            return out
        x, y = x + direction[0] * jump, y + direction[1] * jump
