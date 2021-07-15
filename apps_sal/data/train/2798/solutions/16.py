def to_alternating_case(string):
    temp = ''
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            temp += chr(ord(i) + 32)
        elif ord(i) >= 97 and ord(i) <= 122:
            temp += chr(ord(i) - 32)
        else:
            temp += i
    return temp
