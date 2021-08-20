def add_binary(a, b):
    return convert_to_binary(a + b)


def convert_to_binary(a):
    remainders = []
    while a // 2 != 0:
        remainders.append(str(a % 2))
        a = a // 2
    return '1' + ''.join(remainders[::-1])
