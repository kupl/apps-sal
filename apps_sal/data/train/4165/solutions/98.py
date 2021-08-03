def uni_total(string):
    if string == "":
        return 0

    count = 0
    for i in string:
        count = count + ord(i)
    return count
