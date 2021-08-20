def interpreter(code, array):
    array = list(map(int, array))
    ptr = step = 0
    while ptr < len(array):
        command = code[step]
        if command == '1':
            array[ptr] ^= 1
        elif command == '0':
            ptr += 1
        step = (step + 1) % len(code)
    return ''.join(map(str, array))
