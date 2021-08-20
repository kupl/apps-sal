def dont_give_me_five(s, e):
    return sum(('5' not in str(e) for e in range(s, e + 1)))
