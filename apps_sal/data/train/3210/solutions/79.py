def get_strings(city):
    l = []
    [l.append(f"{x}:{city.lower().count(x) * '*'}") for x in city.lower() if f"{x}:{city.lower().count(x) * '*'}" not in l and x != ' ']
    return ','.join(l)
