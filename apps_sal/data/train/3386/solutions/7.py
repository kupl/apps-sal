def get_column_title(num):
    if num <= 0:
        raise 'IndexError'
    elif type(num) != int:
        raise 'TypeError'
    else:
        string = ''
        while num > 0:
            (num, remainder) = divmod(num - 1, 26)
            string = chr(65 + remainder) + string
        return string
