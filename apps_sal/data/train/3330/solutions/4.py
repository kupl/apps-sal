def make_triangle(m, n):
    """
    makeTriangle produces a ∆ in a special sequence of numbers.
    m is the starting point and n is the finishibg one.
    The final digit of each number is taken as a character in making the ∆.
    This functions returns a ∆ as a string if possible with the given input else, returns an empty string.
    """

    if (type(m) != type(0)) or (type(n) != type(0)):
        raise TypeError("m and n should be int")
    if m >= n:
        raise ValueError("m not < n")

    chars = [str(i)[-1] for i in range(m, n + 1)]

    row, charc = 0, 0

    while True:
        row += 1
        charc = 0
        for j in range(1, row):
            charc += j
        if len(chars) == charc:
            row -= 1
            break
        if len(chars) < charc:
            return ''

    lor = [[' ' for j in range(i)] for i in range(1, row + 1)]
    i1, sp, b = 0, 0, -1
    c = 2
    i2, l = row - c, 0
    i3, j = row - 2, 0
    while True:
        if len(chars) == 0:
            break
        while i1 <= row - 1:
            lor[i1][b] = chars[0]
            chars.pop(0)
            i1 += 1
        i1 = sp + 2
        b -= 1
        if len(chars) == 0:
            break
        while i2 >= l:
            lor[row - 1][i2] = chars[0]
            chars.pop(0)
            i2 -= 1
        row -= 1
        c += 1
        i2 = row - c
        l += 1
        if len(chars) == 0:
            break
        while i3 > sp:
            lor[i3][j] = chars[0]
            chars.pop(0)
            i3 -= 1
        i3 = row - 2
        j += 1
        sp += 2
    l = ''
    for i in lor:
        if i == lor[0]:
            l += ' ' * (len(lor) - len(i)) + i[0] + '\n'
            continue
        for j in range(len(i)):
            if j == 0:
                l += ' ' * (len(lor) - len(i)) + i[j] + ' '
            elif j == len(i) - 1:
                l += i[j]
            else:
                l += i[j] + ' '
        if i != lor[-1]:
            l += '\n'
    return l
