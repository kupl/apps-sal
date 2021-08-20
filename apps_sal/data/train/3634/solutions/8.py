def reverse_it(data):
    if type(data) == str:
        string = data[::-1]
        return string
    elif type(data) == int:
        integer = int(str(data)[::-1])
        return integer
    elif type(data) == float:
        floater = float(str(data)[::-1])
        return floater
    elif type(data) == abs:
        abso = abs(str(data)[::-1])
        return floater
    else:
        return data


reverse_it('Hello')
reverse_it(12345)
reverse_it(1231.123213)
reverse_it([1, 2, 3, 4])
