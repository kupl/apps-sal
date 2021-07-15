def increment_string(strng):
    if not strng:
        return "1"
    end_idx = len(strng) - 1
    digit_str = ''
    while end_idx >= 0:
        if not strng[end_idx].isdigit():
            break
        digit_str = strng[end_idx] + digit_str
        end_idx -= 1

    if not digit_str.isdigit():
        increment_str = "1"
    elif digit_str[0] != '0':
        increment_str = str(int(digit_str) + 1)
    elif int(digit_str) == 0:
        increment_str = (len(digit_str) - 1) * '0' + '1'
    else:
        len_digit_str = len(digit_str)
        start_idx = 0
        while start_idx < len_digit_str:
            if digit_str[start_idx] != '0':
                break
            start_idx += 1
        increment = str(int(digit_str[start_idx:]) + 1)
        increment_str = (len_digit_str - len(increment)) * '0' + increment

    return strng[0:end_idx+1]+increment_str

