def get_strings(city):
    s, city = str(), ''.join(city.lower().split())
    for i in city:
        if i not in s:
            s+= i+':'+'*'*city.count(i)+','
    return s[:-1]
