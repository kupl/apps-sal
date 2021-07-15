def bonus_time(salary, bonus):
    a = lambda s, b: "${}".format(s*10) if b== True else "${}".format(s)
    return a(salary, bonus)
