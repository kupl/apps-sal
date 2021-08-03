def dont_give_me_five(start, end):
    l = (end + 1 - start) - sum([1 for i in range(start, end + 1) if "5" in str(i)])
    return l
