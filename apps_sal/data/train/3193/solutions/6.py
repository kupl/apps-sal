def create_line(number):
    nums_for_line = [num if num < 10 else num % 10 for num in range(1, number + 1)]
    result = nums_for_line + nums_for_line[::-1]
    return ' '.join(map(str, result))


def stairs(number):
    lines = [create_line(num) for num in range(1, number + 1)]
    max_length = number * 4 - 1
    return '\n'.join(line.rjust(max_length) for line in lines)
