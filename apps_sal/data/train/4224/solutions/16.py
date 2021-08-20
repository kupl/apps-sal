def dont_give_me_five(s, e):
    return sum(('5' not in str(i) for i in range(s, e + 1)))
