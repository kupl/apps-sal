from collections import Counter
def get_strings(city):
    return ','.join((a+f':{"*" * b}' for a,b in Counter(city.lower().replace(' ', '')).items()))
