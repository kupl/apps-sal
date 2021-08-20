def reverse_letter(string):
    lst = list(string)
    lst.reverse()
    newlst = []
    for item in lst:
        if not item.isalpha():
            pass
        else:
            newlst.append(item)
    return ''.join(newlst)
