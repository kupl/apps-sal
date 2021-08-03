def jumping_number(number):
    n = str(number)
    for i in range(len(n) - 1):
        if int(n[i]) + 1 != int(n[i + 1]) and int(n[i]) - 1 != int(n[i + 1]):
            return "Not!!"
    return "Jumping!!"
