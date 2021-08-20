rule = ['0', '1', '1', '1', '1', '0', '0', '0']


def rule30(list_, n):
    res = ''.join(('1' if x == 1 else '0' for x in list_))
    for _ in range(n):
        res = '00' + res + '00'
        res = ''.join((rule[int(res[i:i + 3], 2)] for i in range(len(res) - 2)))
    return list(map(int, res))
