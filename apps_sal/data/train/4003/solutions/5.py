def possible_positions(pos):
    abc = 'abcdefgh'
    x, y = abc.index(pos[0]), int(pos[1])
    l = [[x + 2, y - 1], [x + 2, y + 1], [x - 2, y - 1], [x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x - 1, y - 2], [x + 1, y - 2]]
    m = sorted(filter(lambda x: 0 <= x[0] <= 7 and 1 <= x[1] <= 8, l), key=lambda x: (x[0], x[1]))
    return list(map(lambda x: ''.join([abc[x[0]], str(x[1])]), m))
