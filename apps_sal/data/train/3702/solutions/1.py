def olympic_ring(string):
    rings = string.translate(str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    '1201000000000011110000000011011010000000111000000000'))
    score = sum(map(int, rings)) // 2
    return ['Not even a medal!', 'Bronze!', 'Silver!', 'Gold!']\
                [(score > 1) + (score > 2) + (score > 3)]
