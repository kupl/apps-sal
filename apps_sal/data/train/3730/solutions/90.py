def capitalize(str):
    resArr = []

    def one(string):
        resStr = ""
        for index in range(len(string)):
            if index % 2 == False:
                resStr = resStr + string[index].upper()
            else:
                resStr = resStr + string[index].lower()
        return resStr

    def two(string):
        resStr = ""
        for index in range(len(string)):
            if index % 2 == False:
                resStr = resStr + string[index].lower()
            else:
                resStr = resStr + string[index].upper()
        return resStr
    resArr.append(one(str))
    resArr.append(two(str))
    return resArr
