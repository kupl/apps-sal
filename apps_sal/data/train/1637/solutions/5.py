def encode(s):

    def shift(st, l):
        res = list(s)
        for i in range(l):
            res.insert(0, res.pop())
        return res
    matrix = []
    for i in range(len(s)):
        matrix.append(shift(s, i))
    matrix.sort()
    out = []
    number = 0
    for i in range(len(matrix)):
        out.append(matrix[i][-1])
        if matrix[i] == list(s):
            number = i
    return (''.join(out), number)


def decode(string, number):
    if string == '':
        return ''

    def AppenderAndSorter(matrix, arr):
        for i in range(len(arr)):
            matrix[i].insert(0, arr[i])
        matrix.sort()
    matrix = []
    for i in range(0, len(string)):
        matrix.append([string[i]])
    matrix.sort()
    for i in range(1, len(string)):
        AppenderAndSorter(matrix, string)
    out = ''.join(matrix[number])
    return ''.join(out)
