def bits_battle(numbers):
    res = [0, 0]
    for x in numbers:
        res[x & 1] += bin(x)[2:].count('01'[x & 1])
    return 'odds win' if res[0] < res[1] else 'evens win' if res[0] > res[1] else 'tie'
