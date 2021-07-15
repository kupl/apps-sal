from collections import Counter
def get_strings(city):
    lst = []
    for key, value in dict(Counter(city.replace(' ', '').lower())).items():
        lst.append(key+':'+'*'*value)
    return ','.join(lst)
