def parse_float(string):
    if isinstance(string, str):
        stringList = string.split('.')
        if len(stringList) == 2 and all(x.isdigit for x in stringList):
            return float(stringList[0] + '.' + stringList[1])
        else:
            return None
    else:
        return None
