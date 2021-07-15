def to_bits(string):
    bitmap = [0] * 5000
    for x in map(int, string.split()):
        bitmap[x] = 1
    return bitmap
