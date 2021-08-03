def dont_give_me_five(start, end):
    return sum(1 for i in range(start, end + 1) if '5' not in str(i))
