import re


def poohbear(code):
    data, ptr, step, clipboard, stack, loop, output = {}, 0, 0, 0, [], {}, []

    code = re.sub('[^+-><cpWEPNTQULIVABYD]', '', code)

    for i, command in enumerate(code):
        if command == 'W':
            stack.append(i)
        elif command == 'E':
            start = stack.pop()
            loop[start], loop[i] = i, start

    while step < len(code):
        data[ptr] = data.get(ptr, 0)

        command = code[step]
        if command == '+':
            data[ptr] += 1
        elif command == '-':
            data[ptr] -= 1
        elif command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == 'c':
            clipboard = data[ptr]
        elif command == 'p':
            data[ptr] = clipboard
        elif command == 'W' and data[ptr] == 0:
            step = loop[step]
        elif command == 'E' and data[ptr] != 0:
            step = loop[step]
        elif command == 'P':
            output.append(chr(data[ptr]))
        elif command == 'N':
            output.append(str(data[ptr]))
        elif command == 'T':
            data[ptr] *= 2
        elif command == 'Q':
            data[ptr] **= 2
        elif command == 'U':
            data[ptr] = int(data[ptr] ** 0.5)
        elif command == 'L':
            data[ptr] += 2
        elif command == 'I':
            data[ptr] -= 2
        elif command == 'V':
            data[ptr] //= 2
        elif command == 'A':
            data[ptr] += clipboard
        elif command == 'B':
            data[ptr] -= clipboard
        elif command == 'Y':
            data[ptr] *= clipboard
        elif command == 'D':
            data[ptr] //= clipboard

        if ptr in data:
            data[ptr] %= 256
        step += 1

    return ''.join(output)
