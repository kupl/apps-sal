def how_many_bees(hive):
    try:
        right = sum((line.count('bee') for line in map(''.join, hive)))
        left = sum((line.count('eeb') for line in map(''.join, hive)))
        down = sum((line.count('bee') for line in map(''.join, zip(*hive))))
        up = sum((line.count('eeb') for line in map(''.join, zip(*hive))))
        return up + down + left + right
    except TypeError:
        return 0
