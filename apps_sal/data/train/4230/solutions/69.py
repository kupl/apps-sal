def reverse_letter(string):
    li = []
    for i in string:
        if i.isalpha():
            li.append(i)
        else:
            pass
    return "".join(li[::-1])
