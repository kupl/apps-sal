def get_strings(city):
    city = city.lower()
    return ','.join((f"{c}:{'*' * city.count(c)}" for c in dict.fromkeys(city) if c.isalpha()))
