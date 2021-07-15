def array(string):
    splitted = []
    if string == '':
        return None
    else: 
        splitted = string.split(",")
        if len(splitted) < 3:
            return None
        else: 
            splitted = splitted[1:]
            splitted = splitted[:-1]
            result = ''
            i = 1
            for x in splitted:
                result = result + x
                if i != len(splitted):
                    result = result + " "
                i = i + 1
            return result
