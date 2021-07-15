from collections import OrderedDict
def get_strings(city):
    values = [i for i in city.replace(' ','').lower()]
    v2 = [j +':'+'*'*values.count(j) for j in values]
    return ','.join(list(OrderedDict.fromkeys(v2)))
