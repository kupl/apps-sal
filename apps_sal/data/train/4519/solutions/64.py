def max_number(number):
    number_list = [x for x in str(number)]
    new_string = ''
    while number_list:
        for x in number_list:
            if x == max(number_list):
                new_string += x
                number_list.remove(x)
    return int(new_string)
