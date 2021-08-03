def reverse_it(data):
    if type(data) == str:
        return data[::-1]
    elif type(data) == int:
        return int(str(data)[::-1])
    elif type(data) == float:
        return float(str(data)[::-1])
    else:
        return data
