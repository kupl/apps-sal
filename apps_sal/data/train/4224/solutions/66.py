def dont_give_me_five(s,e):
    return len([i for i in range(s, 1+e) if '5' not in str(i)])
