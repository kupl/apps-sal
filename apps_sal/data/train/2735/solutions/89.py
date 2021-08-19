def jumping_number(n):
    n = str(n)
    return 'Jumping!!' if all((abs(int(n[i + 1]) - int(n[i])) == 1 for i in range(len(n) - 1))) or int(n) < 9 else 'Not!!'
