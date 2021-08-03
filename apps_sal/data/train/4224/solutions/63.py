def dont_give_me_five(s, e):
    return len([x for x in range(s, e + 1) if not str(x).count('5')])
