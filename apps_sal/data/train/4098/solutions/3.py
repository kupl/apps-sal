def new_numeral_system(number):
    system = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = system.index(number)
    return ["{} + {}".format(system[i], system[n-i]) for i in range(n // 2 + 1)]

