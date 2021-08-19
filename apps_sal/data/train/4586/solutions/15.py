REMOTE = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'


def tv_remote(word):
    (x, y, total) = (0, 0, 0)
    for char in word:
        pos = REMOTE.index(char)
        (charx, chary) = (pos % 8, pos // 8)
        total += 1 + abs(charx - x) + abs(chary - y)
        (x, y) = (charx, chary)
    return total
