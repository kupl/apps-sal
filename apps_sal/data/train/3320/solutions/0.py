l = {'one': 5, 'two': 4, 'three': 3, 'four': 2, 'five': 1, 'six': 0}
y = {'hhh': '----o----', 'hht': '---- ----', 'htt': '---------', 'ttt': '----x----'}


def oracle(arr):
    s = [''] * 6
    for x in arr:
        s[l[x[0]]] = y[''.join(sorted(x[1:]))]
    return '\n'.join(s)
