def collatz_steps(n, steps):
    while True:
        str = ''
        result = n
        while bool(str != steps) ^ bool(str != steps[:len(str)]):
            if result % 2 == 0:
                result = result / 2
                str += 'D'
            else:
                result = (3 * result + 1) / 2
                str += 'U'
        if str != steps:
            n += 2 ** (len(str) - 1)
        else:
            return n
