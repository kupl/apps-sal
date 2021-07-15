def alternate_sort(list):
    positive_list = []
    negative_list = []
    for number in list:
        if number >= 0:
            positive_list.append(number)
        else:
            negative_list.append(number)
    positive_list.sort()
    negative_list.sort(reverse = True)
    i = 0
    for negative in negative_list:
        positive_list.insert(i * 2, negative)
        i += 1
    return positive_list

