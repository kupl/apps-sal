def reverse_words(text):
    print(text)
    a = list(enumerate(text))
    new_list = []
    new_list2 = []
    x = text.split()
    for el in x:
        new_list.append(list(reversed(el)))
    for el in new_list:
        y = ''.join(el)
        new_list2.append(y)
    new_list3 = [i for ele in new_list2 for i in ele]
    for el in a:
        if el[1] == ' ':
            new_list3.insert(el[0], ' ')
    z = ''.join(new_list3)
    return z
