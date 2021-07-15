def add_binary(a,b):
    return convert_to_binary(a + b)[::-1]

def convert_to_binary(num):
    if num == 0:
        return '1'
    elif num == 1:
        return '1'
    elif num % 2 == 0:
        return '0' + convert_to_binary(num / 2)
    else:
        return '1' + convert_to_binary(num - 1)[1:]
