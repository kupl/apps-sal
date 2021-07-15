def multi_table(number):
    lines = []
    for i in range(1, 11):
        lines.append(f'{i} * {number} = {i * number}')
    return '\n'.join(lines)
