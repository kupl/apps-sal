def unusual_sort(array):
    int_list = []
    digit_list = []
    char_list = []

    for x in array:
        if type(x) is str:
            if x.isdigit():
                digit_list.append(x)
            else:
                char_list.append(x)
        else:
            int_list.append(x)

    int_list.sort()
    digit_list.sort()
    char_list.sort()

    for idx in range(len(int_list)):
        for i in range(len(digit_list)):
            if int_list[idx] <= int(digit_list[i]):
                digit_list.insert(i, int_list[idx])
                break
        else:
            digit_list += int_list[idx:]
            break

    return char_list + digit_list
