def bonus_time(salary, bonus):
    # your code here
    return "${0}{1}".format(salary, "0" if bonus else "")
