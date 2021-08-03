def sort_by_name(arr):
    comparing_list, before_sort_dict, resulty_list = [], {}, []
    nu_dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
               '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
               '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
               '19': 'nineteen'}
    for number in map(str, arr):
        if len(number) == 3:
            if 10 <= int(number[1:]) < 20:
                temp_word = number[1] + number[2]
                numberly_str = '{hundreds} hundred {tens}'.format(hundreds=nu_dict[number[0]], tens=nu_dict[temp_word])
            else:
                numberly_str = '{hundreds} hundred {tens}ty {deci}'.format(hundreds=nu_dict[number[0]],
                                                                           tens=nu_dict[number[1]], deci=nu_dict[number[2]])
        elif len(number) == 2:
            if 10 <= int(number) < 20:
                temp_word = number[0] + number[1]
                numberly_str = '{tens}'.format(tens=nu_dict[temp_word])
            else:
                numberly_str = '{tens}ty {deci}'.format(tens=nu_dict[number[0]], deci=nu_dict[number[1]])
        else:
            if number == '0':
                numberly_str = 'zero'
            else:
                numberly_str = '{deci}'.format(deci=nu_dict[number[0]])
        temp_list = numberly_str.split()
        for pos, word in enumerate(temp_list):
            if word == 'ty':
                temp_list[pos] = ''
        numberly_str = ' '.join(temp_list)
        numberly_str = numberly_str.replace('  ', ' ').replace('fourty', 'forty').replace('twoty', 'twenty')
        numberly_str = numberly_str.replace('threety', 'thirty').replace('fivety', 'fifty').replace('eightty', 'eighty')
        numberly_str = numberly_str.rstrip()
        comparing_list.append(numberly_str)
    for index, crypt in enumerate(comparing_list):
        before_sort_dict[index] = crypt
    sorted_dict = {k: v for k, v in sorted(before_sort_dict.items(), key=lambda item: item[1])}
    for key, value in sorted_dict.items():
        resulty_list.append(arr[key])
    return resulty_list
