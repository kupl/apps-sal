def next_numb(val):
    val += 3 - val % 3
    if not val & 1: val += 3
    while val <= 9876543201:
        s = str(val)
        if len(s) == len(set(s)):
            return val
        val += 6
    return "There is no possible number that fulfills those requirements"
