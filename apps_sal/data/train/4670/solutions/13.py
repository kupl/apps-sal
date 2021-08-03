def string_to_number(s):
    new_list = list(s)
    flag = True
    if new_list[0] == '-':
        new_list.pop(0)
        flag = False

    test_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(0, len(new_list)):
        if new_list[i] not in test_list:
            for j in range(i, len(new_list)):
                new_list.pop(i)
            break

    num_list = new_list[-1::-1]

    total = 0
    for i in range(0, len(num_list)):
        num = int(num_list[i])
        total += num * 10**i
    total = (total if(flag) else -1 * total)

    return total
