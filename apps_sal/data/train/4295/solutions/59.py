def balanced_num(number):
    n = str(number)
    l = (len(n) - 1) // 2
    same = len(n) < 3 or sum(map(int, n[:l])) == sum(map(int, n[-l:]))
    return 'Balanced' if same else 'Not Balanced'
