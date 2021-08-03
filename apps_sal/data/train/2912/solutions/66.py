def find_multiples(integer, limit):
    answ = []
    answer = 0
    n = 1
    while answer < limit:
        answer = integer * n
        if answer <= limit:
            answ.append(answer)
            n += 1
    return answ
