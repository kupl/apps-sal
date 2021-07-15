from collections import Counter

def get_strings(city):
    c = Counter(filter(str.isalpha, city.lower()))
    return ','.join(f'{ k }:{ "*"*v }' for k,v in c.items())
