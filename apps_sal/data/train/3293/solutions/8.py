def rule30(lst, n):
    dic1 = {'000': 0, '001': 1, '010': 1, '011': 1, '100': 1, '101': 0, '110': 0, '111': 0}
    lst = [0] * n + lst + [0] * n
    for _ in range(n):
        temp = lst[:]
        for i in range(0, len(lst)):
            x = [0] + lst[i:i + 2] if i == 0 else lst[i - 1:] + [0] if i == len(lst) - 1 else lst[i - 1:i + 2]
            x = ''.join(map(str, x))
            temp[i] = dic1[x]
        lst = temp[:]
    return lst
