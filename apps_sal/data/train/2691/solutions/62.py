def solve(s):
    str_lst = []
    temp = ""
    for elem in s:
        if elem.isdigit():
            temp += elem
        elif not elem.isdigit() and temp != "":
            str_lst.append(temp)
            temp = ""

    str_lst.append(temp) if temp != "" else False

    maximum = max([int(elem) for elem in str_lst])
    return maximum
