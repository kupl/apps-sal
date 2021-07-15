def get_strings(city):
    city = city.lower().replace(' ', '')
    lst = [f'{x}:{"*" * city.count(x)}' for x in sorted(set(city), key=lambda x: city.index(x))]
    return ','.join(lst)
