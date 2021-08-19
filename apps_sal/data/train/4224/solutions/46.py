def dont_give_me_five(start, end):
    n = []
    for i in range(start, end + 1):
        if i % 5 != 0 or i % 10 == 0:
            if not 50 <= i <= 59:
                if not 150 <= i <= 159:
                    n.append(i)
    return len(n)
