def century(year):
    workshop = list(str(year))
    if len(workshop) > 2:
        if year % 100 == 0:
            return int("".join(workshop[:-2]))
        else:
            return int("".join(workshop[:-2])) + 1
    else:
        return 1
