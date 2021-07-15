def reverse_letter(string):
    list = ''
    list1 = list.join([c for c in string if c.isalpha()])
    return list1[::-1]



