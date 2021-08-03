def disarium_number(n):
    sume = 0
    for i in range(len(str(n))):
        sume += int(str(n)[i])**(i + 1)
    if sume == n:
        return "Disarium !!"
    else:
        return "Not !!"
