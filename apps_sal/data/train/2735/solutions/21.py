def jumping_number(n):
    if n < 10: return "Jumping!!"
    for i in range(len(str(n)) - 1):
        if int(str(n)[i + 1]) not in [int(str(n)[i]) + 1, int(str(n)[i]) - 1]: return "Not!!"
    return "Jumping!!"
