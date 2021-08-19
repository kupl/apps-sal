def balanced_num(n):
    n = '0' + str(n) + '0'
    return 'Balanced' if sum(map(int, n[:len(n) // 2 - (len(n) % 2 == 0)])) == sum(map(int, n[len(n) // 2 + 1:])) else 'Not Balanced'
