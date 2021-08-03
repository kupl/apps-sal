def xor(a, b):
    truCount = 0
    if a:
        truCount += 1
    if b:
        truCount += 1
    if truCount == 1:
        return True
    return False
