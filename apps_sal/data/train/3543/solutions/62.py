def increment_string(strng):
    if len(strng) == 0:
        return "1"

    if not strng[-1].isdigit():
        return strng + "1"
    elif len(strng) == 1:
        return str(int(strng) + 1)

    # Append all non-digit characters to new string, keeping track of the index where characters end
    idx = 0
    for i, c in enumerate(strng):
        if not c.isdigit():
            idx = i

    num_str = strng[idx + 1:]
    inc_num_str = str(int(num_str) + 1)

    return strng[:idx + 1] + inc_num_str.zfill(len(num_str))

    """if len(strng) > 0 and strng[-1].isdigit():
        next_num = int(strng[-1]) + 1
    
        cur_index = -1 # Start at end of string
        
        if next_num < 10:
            strng = strng[:cur_index] + str(next_num)
        else:
            strng = strng[:cur_index] + str(0)
            cur_index -= 1
            
            while (abs(cur_index) <= len(strng)):
                if not strng[cur_index].isdigit():
                    return strng[:cur_index ] + "1" + strng[cur_index:]
                
                cur_num = int(strng[cur_index])
                if cur_num < 9:
                    strng = strng[:cur_index] + str(cur_num + 1) + strng[cur_index + 1:]
                    return strng
                else:
                    strng = strng[:cur_index] + str(0) + strng[cur_index + 1:]
                    cur_index -= 1
    else:
        strng += '1'
                
    return strng
    """
