from math import floor
import random


def interpret(s):
    s, j, k = [[j for j in i] for i in s.splitlines()], 0, -1
    direction, stack, output = 'right', [], []
    while 1:
        if direction == "right":
            k += 1
        elif direction == "left":
            k -= 1
        elif direction == "up":
            j -= 1
        elif direction == "down":
            j += 1
        i = s[j][k]
        if i in "+-*/%`g":
            a, b = stack.pop(), stack.pop()
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(b - a)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(0 if not a else int(floor(b / a)))
        elif i == '%':
            stack.append(0 if not a else b % a)
        elif i == '!':
            stack.append(1 if not stack.pop() else 0)
        elif i == '`':
            stack.append(1 if b > a else 0)
        elif i == '>':
            direction = 'right'
        elif i == "<":
            direction = 'left'
        elif i == "^":
            direction = 'up'
        elif i == 'v':
            direction = 'down'
        elif i == '?':
            direction = random.choice(['right', 'left', 'down', 'up'])
        elif i == '_':
            direction = 'right' if not stack.pop() else 'left'
        elif i == '|':
            direction = 'down' if not stack.pop()else 'up'
        elif i == ':':
            stack.append(0 if not stack else stack[-1])
        elif i == '$':
            stack.pop()
        elif i == '.':
            output.append(stack.pop())
        elif i == ',':
            output.append(chr(stack.pop()))
        elif i == 'p':
            y, x, v = stack.pop(), stack.pop(), stack.pop()
            s[y][x] = chr(v)
        elif i == 'g':
            stack.append(ord(s[a][b]))
        elif i == '\\':
            if len(stack) == 1:
                stack.insert(0, 0)
            else:
                stack[-1], stack[-2] = stack[-2], stack[-1]
        if i == '#':
            if direction == 'right':
                k += 1
            elif direction == 'left':
                k -= 1
            elif direction == 'up':
                j -= 1
            elif direction == 'down':
                j += 1
        if i == '"':
            k += (1 if direction == 'right' else -1)
            while s[j][k] != '"':
                stack.append(ord(s[j][k]))
                k += (1 if direction == 'right' else -1)
        if i == '@':
            break
    return "".join(map(str, output))
