def sum_of_a_beach(beach):
    return sum([beach.lower().count(element) for element in ['sand', 'water', 'fish', 'sun']])
