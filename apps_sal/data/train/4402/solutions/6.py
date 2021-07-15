def solve(st):
    a = ''.join(sorted(st))
    if a in 'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False

