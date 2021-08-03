def is_magical(sq):
    c = sum(sq[:3])
    ls = [sq[i:i + 3] for i in range(0, 9, 3)]
    ls2 = list(zip(*ls))
    if sum([ls[i][i] for i in range(3)]) != sum([ls[i][2 - i] for i in range(3)]):
        return False
    return True if ([sum(i) for i in ls] + [sum(i) for i in ls2]).count(c) == 6 else False
