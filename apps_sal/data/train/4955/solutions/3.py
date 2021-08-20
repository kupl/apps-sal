def ride(group, comet):
    command = {True: 'GO', False: 'STAY'}

    def num(st):
        return reduce(lambda x, y: x * y, map(lambda x: ord(x) - ord('A') + 1, st)) % 47
    return command[num(group) == num(comet)]
