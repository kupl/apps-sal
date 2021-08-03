def decode_resistor_colors(bands):
    dic = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
           'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9}
    lst = bands.split()
    num = dic[lst[0]] * 10 + dic[lst[1]]
    numbe = num * 10**dic[lst[2]]
    if len(lst) > 3:
        if lst[3] == "gold":
            tol = 5
        elif lst[3] == "silver":
            tol = 10
    else:
        tol = 20
    if numbe >= 1000000:
        if numbe % 1000000 == 0:
            number = numbe // 1000000
        else:
            number = numbe / 1000000
        return str(number) + "M ohms, " + str(tol) + "%"
    elif numbe >= 1000:
        if numbe % 1000 == 0:
            number = numbe // 1000
        else:
            number = numbe / 1000
        return str(number) + "k ohms, " + str(tol) + "%"
    else:
        number = numbe
        return str(number) + " ohms, " + str(tol) + "%"
