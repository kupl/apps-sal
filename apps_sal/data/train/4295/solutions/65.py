def balanced_num(number):
    inputlst = list(str(number))
    length = (len((str(number))))

    if length % 2 != 0:
        middlechartoremove = int(length / 2)
        del inputlst[middlechartoremove]
        inputlst = list(map(int, inputlst))
        oneside = inputlst[middlechartoremove:]
        anotherside = inputlst[:middlechartoremove]
        if sum(oneside) == sum(anotherside):
            return "Balanced"
        else:
            return "Not Balanced"

    else:
        middlechartoremove = int(length / 2)
        secondchartoremove = middlechartoremove - 1
        del inputlst[middlechartoremove]
        inputlst = list(map(int, inputlst))
        oneside = inputlst[secondchartoremove + 1:]
        anotherside = inputlst[:secondchartoremove:]

        if sum(oneside) == sum(anotherside):
            return "Balanced"
        else:
            return "Not Balanced"
