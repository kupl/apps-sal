def balanced_num(number):
    left_number = 0
    right_number = 0
    number_string = str(number)
    number_length = len(number_string)
    if number_length < 3:
        return 'Balanced'
    else:
        reverse_number = number_string[::-1]
        if number_length % 2 == 0:
            n = 2
        else:
            n = 1
        for i in range(int((number_length - n) / 2)):
            left_number += int(number_string[i])
            right_number += int(reverse_number[i])
        if left_number == right_number:
            return 'Balanced'
        else:
            return 'Not Balanced'
