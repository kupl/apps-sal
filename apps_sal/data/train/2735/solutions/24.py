def jumping_number(n):
    l = len(str(n))
    if l == 1:
        return 'Jumping!!'
    x = [int(x) for x in str(n)]
    return 'Jumping!!' if all((abs(x[i + 1] - x[i]) == 1 for i in range(l - 1))) else 'Not!!'
