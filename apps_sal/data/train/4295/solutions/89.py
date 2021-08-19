def balanced_num(n):
    n = str(n)
    if len(n) % 2 == 0:
        return ['Not Balanced', 'Balanced'][sum(map(int, n[:len(n) // 2 - 1])) == sum(map(int, n[len(n) // 2 + 1:]))]
    else:
        return ['Not Balanced', 'Balanced'][sum(map(int, n[:len(n) // 2])) == sum(map(int, n[len(n) // 2 + 1:]))]
