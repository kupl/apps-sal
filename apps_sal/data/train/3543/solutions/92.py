def increment_string(strng):
    if strng == "": return "1"
    if strng.isdigit(): return str(int(strng) + 1).rjust(len(strng), "0")
    index = -1
    while strng[index].isdigit():
        index -= 1
    if index == -1: return strng + "1"
    data = [strng[:index + 1], strng[index + 1:]]
    data[1] = str(int(data[1]) + 1).rjust(len(data[1]), "0")
    return ''.join(data)
