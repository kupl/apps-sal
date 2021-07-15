from collections import Counter

def get_strings(city):
    return ','.join([f"{char}:{'*' * char_count}" for (char, char_count) 
        in list(dict(Counter(city.lower())).items()) if char != ' ' ])

