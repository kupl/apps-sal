seq = [1, 2, 3, 'cat']
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False

print(check(seq, 4))
