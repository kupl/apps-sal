def print_number(number, char):
    separator_arr = [' ' for i in range(10)]
    separator_arr[0] = char
    separator_arr[9] = char
    border_arr = [char for i in range(10)]
    char_2 = char * 2
    char_3 = char * 3
    char_4 = char * 4
    char_5 = char * 5
    char_6 = char * 6
    space_2 = ' ' * 2
    space_3 = ' ' * 3
    space_4 = ' ' * 4
    space_6 = ' ' * 6
    sccccs = f' {char_4} '
    ccsscc = f'{char_2}{space_2}{char_2}'
    ssccss = f'{space_2}{char_2}{space_2}'
    sssccs = f'{space_3}{char_2} '
    sccsss = f' {char_2}{space_3}'
    sssscc = f'{space_4}{char_2}'
    ccssss = f'{char_2}{space_4}'
    cccccs = f'{char_5} '
    sssccs = f'{space_3}{char_2} '
    digits = {
        '0': [char_6, space_6, sccccs, ccsscc, ccsscc,
              ccsscc, ccsscc, sccccs, space_6, char_6],
        '1': [char_6, space_6, ssccss, f' {char_3}{space_2}', f'{char} {char_2}{space_2}',
              ssccss, ssccss, char_6, space_6, char_6],
        '2': [char_6, space_6, sccccs, ccsscc, sssccs,
              ssccss, sccsss, char_6, space_6, char_6],
        '3': [char_6, space_6, sccccs, ccsscc, sssccs,
              sssccs, ccsscc, sccccs, space_6, char_6],
        '4': [char_6, space_6, ccsscc, ccsscc, ccsscc,
              f' {char_5}', sssscc, sssscc, space_6, char_6],
        '5': [char_6, space_6, char_6, ccssss, cccccs,
              sssscc, sssscc, cccccs, space_6, char_6],
        '6': [char_6, space_6, sssccs, ssccss, sccccs,
              ccsscc, ccsscc, sccccs, space_6, char_6],
        '7': [char_6, space_6, char_6, ccsscc, sssccs,
              ssccss, sccsss, sccsss, space_6, char_6],
        '8': [char_6, space_6, sccccs, ccsscc, sccccs,
              sccccs, ccsscc, sccccs, space_6, char_6],
        '9': [char_6, space_6, sccccs, ccsscc, ccsscc,
              sccccs, ssccss, sccsss, space_6, char_6],
    }

    def normalize(n):
        if n > 9999:
            return str(n)
        else:
            return str(n).rjust(5, '0')
    num = normalize(number)
    final_result = []
    for i in range(10):
        final_result.append(f'{border_arr[i]}{separator_arr[i]}{separator_arr[i]}{digits[num[0]][i]}{separator_arr[i]}'
                            f'{digits[num[1]][i]}{separator_arr[i]}{digits[num[2]][i]}{separator_arr[i]}'
                            f'{digits[num[3]][i]}{separator_arr[i]}{digits[num[4]][i]}{separator_arr[i]}{separator_arr[i]}{border_arr[i]}')

    return '\n'.join(final_result)
