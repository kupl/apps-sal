def balanced_num(number):
    n = str(number)
    L = len(n)
    if L % 2 == 1:
        m = (L - 1) // 2
        n = n[:m] + n[m + 1:]
    else:
        m = L // 2
        n = n[:m - 1] + n[m + 1:]
    L = len(n)
    (left, right) = (n[:L // 2], n[L // 2:])
    if sum([int(i) for i in left]) == sum([int(i) for i in right]):
        return 'Balanced'
    else:
        return 'Not Balanced'
