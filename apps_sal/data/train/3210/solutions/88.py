from collections import Counter
def get_strings(city):
    return ','.join(f'{k}:{"*"*v}' for k, v in Counter(city.lower().replace(' ','')).items())
