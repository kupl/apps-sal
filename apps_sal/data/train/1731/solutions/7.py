from random import choice
# 题目太复杂,跳过这个题


def interpret(code):
    code = [list(l) for l in code.split('\n')]
    x, y = 0, 0
    dx, dy = 1, 0
    output = ''
    stack = []
    string_mode = False

    while True:
        move = 1
        i = code[y][x]

        if string_mode:
            if i == '"':
                string_mode = False
            else:
                stack.append(ord(i))
        else:

            if i.isdigit():
                stack.append(int(i))
            elif i == '+':
                stack[-2:] = [stack[-2] + stack[-1]]
            elif i == '-':
                stack[-2:] = [stack[-2] - stack[-1]]
            elif i == '*':
                stack[-2:] = [stack[-2] * stack[-1]]
            elif i == '/':
                stack[-2:] = [stack[-2] and stack[-2] / stack[-1]]
            elif i == '%':
                stack[-2:] = [stack[-2] and stack[-2] % stack[-1]]
            elif i == '!':
                stack[-1] = not stack[-1]
            elif i == '`':
                stack[-2:] = [stack[-2] > stack[-1]]
            elif i in '><^v?':
                if i == '?':
                    i = choice('><^v')
                if i == '>':
                    dx, dy = 1, 0
                elif i == '<':
                    dx, dy = -1, 0
                elif i == '^':
                    dx, dy = 0, -1
                elif i == 'v':
                    dx, dy = 0, 1
            elif i == '_':
                dx, dy = (-1 if stack.pop() else 1), 0
            elif i == '|':
                dx, dy = 0, (-1 if stack.pop() else 1)
            elif i == '"':
                string_mode = True
            elif i == ':':
                stack.append(stack[-1] if stack else 0)
            elif i == '\\':
                stack[-2:] = stack[-2:][::-1]
            elif i == '$':
                stack.pop()
            elif i == '.':
                output += str(stack.pop())
            elif i == ',':
                output += chr(stack.pop())
            elif i == '#':
                move += 1
            elif i == 'p':
                ty, tx, tv = stack.pop(), stack.pop(), stack.pop()
                code[ty][tx] = chr(tv)
            elif i == 'g':
                ty, tx = stack.pop(), stack.pop()
                stack.append(ord(code[ty][tx]))
            elif i == '@':
                return output

        for _ in range(move):
            x = (x + dx) % len(code[y])
            y = (y + dy) % len(code)
