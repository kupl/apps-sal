def dont_give_me_five(s, e):
    cnt = 0
    for i in range(s, e + 1):
        if "5" not in str(i):
            cnt += 1
    return cnt
