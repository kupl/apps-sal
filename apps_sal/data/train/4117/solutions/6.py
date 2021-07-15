def sum_from_string(string):
    str_nr, all_nr, have_nr = '', [], False
    for item in string + '_':
        if '0' <= item <= '9':
            str_nr += item
            have_nr = True
        else:
            if have_nr:
                all_nr.append(int(str_nr))
                have_nr , str_nr = False, ''
    return sum(all_nr)
