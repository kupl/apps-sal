def jumping_number(n):
    a = str(n)
    return 'Jumping!!' if len([1 for x in range(len(a) - 1) if int(a[x + 1]) not in (int(a[x]) + 1, int(a[x]) - 1)]) == 0 else 'Not!!'
