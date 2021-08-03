def dont_give_me_five(start, end):
    n = [i for i in range(start, end + 1) if str(i).count('5') == 0]
    return len(n)
