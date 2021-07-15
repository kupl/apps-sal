def get_strings(city):
    result = ''
    d = {}
    for letter in city.lower():
        d[letter] = d.get(letter, 0) + 1
    for letter in city.lower().replace(' ',''): 
        if not letter in result: 
            result += letter+':'+'*'*d[letter]+','
    return result[:-1]
