def round_it(n):
    return int(n // 1) if len(str(n).split('.')[0]) > len(str(n).split('.')[1]) else int(n // 1 + 1) if len(str(n).split('.')[0]) < len(str(n).split('.')[1]) else round([round(n, x) for x in list(range(len(str(n).split('.')[1]), 0, -1))][-1])
