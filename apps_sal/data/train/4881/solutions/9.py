def camelize(string):
    s = ""
    for i in string.lower():
        if i in "qwertyuiopasdfghjklzxcvbnm1234567890":
            s += i
        else:
            s += " "
    s = s.split()
    lst = []
    for i in s:
        lst.append(i[0].upper() + i[1:])
    return "".join(lst)

