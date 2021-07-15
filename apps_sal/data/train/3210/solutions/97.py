import json
def get_strings(city):
    cityAmount = {}
    for x in range(len(city)):
        if city[x] == ' ':
            continue
        if city[x].lower() in cityAmount:
            cityAmount[city[x].lower()] += '*'
        else:
            cityAmount[city[x].lower()] = '*'
    return ",".join(("{}:{}".format(*i) for i in list(cityAmount.items())))

