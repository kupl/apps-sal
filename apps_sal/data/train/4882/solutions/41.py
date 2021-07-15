def round_to_next5(n):
    for i in range(5):
        a = n + i
        if a / 5 == a //5:
            return a
