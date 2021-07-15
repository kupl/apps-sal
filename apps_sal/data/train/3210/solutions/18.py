def get_strings(city):
    
    ciu = {}
    
    for letra in city.lower().replace(" ",""):
        if letra not in ciu:
            ciu[letra] = "*"
        else: 
            ciu[letra] += "*"
    
    
    array = []
    for clave in ciu:
        
        array.append("{}:{}".format(clave, ciu[clave]))
        
    return ",".join(array).replace(" ","")


