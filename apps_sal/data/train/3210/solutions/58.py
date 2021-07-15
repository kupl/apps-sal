def get_strings(city):
    l = []
    city = city.lower()
    city = city.replace(" ","")
    for char in city:
        ast = city.count(char) * "*"
        l.append("%s:%s," %(char,ast))        
    l = list(dict.fromkeys(l))
    city = "".join(l)
    return city[0:-1]

