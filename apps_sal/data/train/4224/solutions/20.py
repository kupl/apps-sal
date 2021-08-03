def dont_give_me_five(start, end):
    return len((list(filter(lambda i: not "5" in str(i), range(start, end + 1)))))
