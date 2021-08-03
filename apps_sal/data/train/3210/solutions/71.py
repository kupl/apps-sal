def get_strings(city):
    city = city.lower()
    return ','.join([f"{k}:{v}" for k, v in {c: '*' * city.count(c) for c in city if c != " "}.items()])
