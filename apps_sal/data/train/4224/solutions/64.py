def dont_give_me_five(start, end):
    m = [i for i in range(start, end + 1) if "5" not in str(i)]
    return len(m)
