import json
def get_strings(city):
    city = city.lower()
    city = city.replace(" ","")
    c = {}
    for i in city:
        if i in c:
            c[i] += "*"
        else:
            c[i] = "*"
    
    final = json.dumps(c)
    final = (final.replace("{","").replace("}","").replace(" ","").replace('"',""))
            
    return final
