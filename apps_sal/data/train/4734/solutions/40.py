def bonus_time(salary, bonus):
    def a(s, b): return "${}".format(s * 10) if b == True else "${}".format(s)
    return a(salary, bonus)
