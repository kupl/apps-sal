def dont_give_me_five(x, y):
    return len([i for i in range(x, y + 1) if '5' not in str(i)])
