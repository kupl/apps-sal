def fouriest(numb):
    ans = ""
    temp = 0
    baz = 0
    for i in range(5, 300):
        converted_string, modstring = "", ""
        currentnum = numb
        base = i
        while currentnum:
            mod = currentnum % base
            currentnum = currentnum // base
            converted_string = chr(48 + mod + 7 * (mod > 10)) + converted_string
        if str(converted_string).count("4") > temp:
            temp = str(converted_string).count("4")
            ans = str(converted_string)
            baz = i
    ans = "".join([i if i.isdigit() else "x" for i in str(ans)])
    return "{} is the fouriest ({}) in base {}".format(numb, ans, baz)
