def dont_give_me_five(start, end):
    n = 0
    for j in range(start, end + 1):
        i = abs(j)
        n += 1
        while i // 5 > 0:
            if i % 5 == 0 and i % 10 != 0:
                n -= 1
                break
            i = i // 10
    return n
