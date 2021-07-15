from collections import Counter

def get_strings(city):
    city = [elem for elem in city.lower() if elem.islower()]
    a = Counter(city)
    return ','.join(f"{elem}:{'*' * a[elem]}" for elem in list(a.keys()))

