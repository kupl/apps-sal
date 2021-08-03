def jumping_number(n):
    n = list(str(n))
    for i in range(len(n) - 1):
        if len(n) == 1:
            return "Jumping!!"
        elif abs(int(n[i]) - int(n[i + 1])) != 1:
            return "Not!!"

    return "Jumping!!"
