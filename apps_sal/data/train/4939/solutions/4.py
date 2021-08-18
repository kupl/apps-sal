import re


def coffee_limits(year, month, day):
    h_cafe = str(year)

    if len(str(month)) == 1:
        h_cafe += "0" + str(month)
    else:
        h_cafe += str(month)

    if len(str(day)) == 1:
        h_cafe += "0" + str(day)
    else:
        h_cafe += str(day)

    h_cafe = int(h_cafe)
    h_decaf = h_cafe
    n = 0
    cafe = 0
    decaf = 0
    print(h_cafe)
    while (n < 5000):
        h_cafe += 51966
        h_decaf += 912559
        n += 1
        if "dead" in hex(h_cafe):
            if cafe == 0:
                cafe = n
        elif "dead" in hex(h_decaf):
            if decaf == 0:
                decaf = n
    return [cafe, decaf]
