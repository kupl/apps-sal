def reverse_and_combine_text(text):
    lst = text.split(' ')
    if len(lst) == 1:
        return text
    while len(lst) != 1:
        lst1 = []
        for i in lst:
            a = ''.join(list(reversed(i)))
            lst1.append(a)
        lst2 = []
        if len(lst) % 2 == 0:
            for x in range(0, len(lst), 2):
                lst2.append(lst1[x] + lst1[x + 1])
            lst = lst2
        else:
            for x in range(0, len(lst) - 1, 2):
                lst2.append(lst1[x] + lst1[x + 1])
            lst2.append(lst1[-1])
            lst = lst2
    return lst[0]
