def bingo(card, numbers):

    rc, cc, dc = [0] * 5, [0] * 5, [1] * 2            # rows count, columns count, diag counts
    rc[2] = cc[2] = 1                           # preaffect 'FREE SPACE'
    s = set(numbers)

    for x, line in enumerate(card[1:]):
        for y, (c, n) in enumerate(zip(card[0], line)):
            tile = f'{c}{n}'
            if tile in s:
                rc[x] += 1
                cc[y] += 1
                if x == y:
                    dc[0] += 1         # main diag
                if x + y == 4:
                    dc[1] += 1         # secundary diag
    return 5 in rc + cc + dc
