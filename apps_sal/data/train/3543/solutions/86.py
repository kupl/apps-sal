def increment_string(strng):
    if strng == '':
        return '1'
    
    print(strng)
    # no number
    num_start = 0
    for i in reversed(list(range(len(strng)))):
        if strng[i].isdigit() == False:
            num_start = i + 1
            break

    if num_start == len(strng):
        return strng + '1'
            
    orig_str = strng[0:num_start]
    num_str = strng[num_start::]
    
    digits = len(num_str)
    suffix_num = str(int(num_str) + 1)
    
    return orig_str + ('0' * (digits - len(suffix_num))) + str(suffix_num)
        

