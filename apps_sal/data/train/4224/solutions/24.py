def dont_give_me_five(start, end):
    k = [str(i) for i in range(start, end + 1)]
    return len([i for i in k if '5' not in i])
