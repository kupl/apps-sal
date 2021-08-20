def solve(s):
    new_list = []
    number = ''
    for characters in s:
        if characters.isdigit():
            number += characters
        elif number != '':
            new_list.append(int(number))
            number = ''
    if number != '':
        new_list.append(int(number))
    return max(new_list)
