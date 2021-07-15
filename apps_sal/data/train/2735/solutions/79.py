def jumping_number(n):
    lst = list(map(int, str(n)))
    return 'Jumping!!' if all(abs(x - y) == 1 for x, y in zip(lst, lst[1:])) else 'Not!!'
