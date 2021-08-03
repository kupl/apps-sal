def array(string):
    first = -1
    last = -1
    for i in range(len(string)):
        if string[i] == ',' and first == -1:
            first = i
        if string[len(string) - i - 1] == ',' and last == -1:
            last = i
    if -last - 1 + len(string) == first or first == -1 or last == -1:
        return None
    return string.replace(' ', '').replace(',', ' ')[first + 1:-last - 1]
