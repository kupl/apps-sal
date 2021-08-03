def capitalize(s):
    even = ''
    odd = ''
    count = 0
    for i in s:
        if count % 2 == 0:
            even += i.upper()
            odd += i
        else:
            even += i
            odd += i.upper()
        count += 1
    lst = []
    lst.append(even)
    lst.append(odd)
    return lst
