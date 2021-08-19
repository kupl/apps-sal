def pattern(n):
    # Happy Coding ^_^
    gtext = ""
    for i in range(1, n + 1):
        s = ""
        for j in range(1, i + 1):
            s += "" + str(i)

        gtext += s
        if(not i == n):
            gtext += "\n"

    return gtext
