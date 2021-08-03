def get_column_title(num):
    if num < 1:
        return error
    a = [num % 26]
    while num > 26:
        num = num // 26 - 1
        a += [num % 26 + 1]
    y = a + [num] if num > 26 else a
    if y[0] == 0 and len(y) > 1:
        y[1] -= 1
    return ''.join(['Z' if i == 0 else chr(i + ord('A') - 1) for i in y][::-1])
