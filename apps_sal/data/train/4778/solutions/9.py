def most_money(students):
    amounts = {s.name: 5*s.fives + 10*s.tens + 20*s.twenties for s in students}
    return "all" if 1 == len(set(amounts.values())) < len(amounts) else max(amounts, key=amounts.get)
