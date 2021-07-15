POS  = {'one': 5, 'two': 4, 'three': 3, 'four': 2, 'five': 1, 'six': 0}
TYPE = {'ttt': 'x', 'htt': '-', 'hht': ' ', 'hhh': 'o'}
LINE = "----{}----"

def oracle(arr):
    lst = [0] * 6
    for params in arr:
        lst[POS[params[0]]] = LINE.format(TYPE[''.join(sorted(params[1:]))])
    return '\n'.join(lst)
