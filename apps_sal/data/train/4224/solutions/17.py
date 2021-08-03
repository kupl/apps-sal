def dont_give_me_five(start, end):
    return len([i for i in list(map(str, range(start, end + 1))) if "5" not in i])
