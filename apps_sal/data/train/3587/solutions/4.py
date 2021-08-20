def original_number(s):
    a = s[:]
    code = [0 for _ in range(10)]
    book = [[0, 'Z', 'ZERO'], [2, 'W', 'TWO'], [6, 'X', 'SIX'], [8, 'G', 'EIGHT'], [7, 'S', 'SEVEN'], [5, 'V', 'FIVE'], [4, 'F', 'FOUR'], [3, 'T', 'THREE'], [1, 'O', 'ONE'], [9, 'E', 'NINE']]
    for i in book:
        code[i[0]] = a.count(i[1])
        for j in i[2]:
            a = a.replace(j, '', code[i[0]])
    return ''.join(('0123456789'[k] * j for (k, j) in enumerate(code)))
