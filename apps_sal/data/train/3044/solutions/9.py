def solve(st):
    for x in range(len(st)):
        if st == st[::-1]:
            return True
        else:
            st = st[1:] + st[0]
    return False
