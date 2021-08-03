import random


def interpret(code):
    output = ""
    coordinates = code.split("\n")
    coordinate = [list(row) for row in coordinates]
    stack = []
    x = 0
    y = 0
    dx = 1
    dy = 0
    a = ""
    temp = 1
    ascii_code = 0
    opened = False
    skip_next = False

    while True:
        command = coordinate[y][x]
        if skip_next:
            skip_next = False
            x += dx
            y += dy
            continue
        elif command.isnumeric():
            stack.append(int(command))
        elif command == '>':
            dx = 1
            dy = 0
        elif command == '<':
            dx = -1
            dy = 0
        elif command == '^':
            dx = 0
            dy = -1
        elif command == 'v':
            dx = 0
            dy = 1
        elif command == '?':
            dx = random.randint(-1, 1)
            if dx != 0:
                dy = 0
            else:
                dy = random.choice([-1, 1])
        elif command == '"':
            opened = not opened
        elif opened:
            stack.append(ord(command))
        elif command == "+":
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)
        elif command == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif command == "*":
            a, b = stack.pop(), stack.pop()
            stack.append(a * b)
        elif command == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a) if a != 0 else 0)
        elif command == "%":
            a, b = stack.pop(), stack.pop()
            stack.append(b % a if a != 0 else 0)
        elif command == "!":
            if int(stack[-1]) == 0:
                stack[-1] = 1
            else:
                stack[-1] = 0
        elif command == "`":
            a, b = stack.pop(), stack.pop()
            if b > a:
                stack.append(1)
            else:
                stack.append(0)
        elif command == "_":
            if stack.pop() == 0:
                dx = 1
                dy = 0
            else:
                dx = -1
                dy = 0
        elif command == "|":
            if stack.pop() == 0:
                dx = 0
                dy = 1
            else:
                dx = 0
                dy = -1
        elif command == ":":
            if len(stack) == 0:
                stack.append(0)
            else:
                stack.append(stack[-1])
        elif command == "\\":
            if len(stack) < 2:
                stack.append(0)
            else:
                a = stack[-1]
                stack[-1] = stack[-2]
                stack[-2] = a
        elif command == "$":
            if len(stack) != 0:
                stack.pop()
        elif command == ".":
            if len(stack) != 0:
                output += str(stack.pop())
        elif command == ",":
            if len(stack) != 0:
                ascii_code = stack[-1]
                output += chr(ascii_code)
            stack.pop()
        elif command == "#":
            skip_next = True
        elif command == "p":
            y1, x1, v = stack.pop(), stack.pop(), stack.pop()
            coordinate[y1][x1] = chr(v)
        elif command == "g":
            y1, x1 = stack.pop(), stack.pop()
            stack.append(ord(coordinate[y1][x1]))
        elif command == '@':
            break
        x += dx
        y += dy
    return output
