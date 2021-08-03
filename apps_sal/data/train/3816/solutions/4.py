A = 'abcdefghijklmnopqrstuvwxyz'


def move_ten(s):
    return ''.join(s.translate(str.maketrans(A, A[10:] + A[:10])))
