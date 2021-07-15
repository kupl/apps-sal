def correct(string):
    newList = []
    for i in list(string):
        if i == "0":
            newList.append("O")
        elif i == "5":
            newList.append("S")
        elif i == "1":
            newList.append("I")
        else:
            newList.append(i)
    return "".join(newList)
