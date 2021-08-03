def century(year):
    if len(str(year)) > 3:
        print(str(year)[len(str(year)) - 1])

        if str(year)[len(str(year)) - 1] == "0" and str(year)[len(str(year)) - 2] == "0":
            return(int(str(year)[:len(str(year)) - 2]))
        else:
            return(int(str(year)[:len(str(year)) - 2]) + 1)

    elif len(str(year)) == 3:
        return(int(str(year)[0]) + 1)
    else:
        return 1
