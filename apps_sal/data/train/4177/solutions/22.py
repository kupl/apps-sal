def men_from_boys(num):
    return sorted(list(set([i for i in num if i % 2 == 0]))) + sorted(list(set([i for i in num if i % 2 != 0])), reverse=True)
