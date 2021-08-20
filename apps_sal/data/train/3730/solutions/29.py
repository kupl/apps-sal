def capitalize(s):
    list_a = list(s)
    temp_list1 = []
    temp_list2 = []
    counter = 0
    for i in list_a:
        if counter % 2 == 0:
            temp_list1.append(chr(ord(list_a[counter]) - 32))
        else:
            temp_list1.append(list_a[counter])
        counter += 1
    temp_str1 = ''.join(temp_list1)
    counter = 0
    for i in list_a:
        if counter % 2 != 0:
            temp_list2.append(chr(ord(list_a[counter]) - 32))
        else:
            temp_list2.append(list_a[counter])
        counter += 1
    temp_str2 = ''.join(temp_list2)
    return [temp_str1, temp_str2]
