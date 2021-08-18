all_num = \
    '''|  
| 
| 
| 
|       |       |  
| 
| 
| 
|  


def segment_display(num):
    all_num_list = all_num.split('\n')
    fish_list = []
    for val in (all_num_list):
        fish_hold_list = []
        fish_hold = '' + '|       |' * (6 - len(str(num)))
        for num2 in str(num):
            num3 = int(num2)
            beg_col = (num3 * 8)
            end_col = beg_col + 9
            fish_hold += val[beg_col:end_col]
            fish_hold_list.append([fish_hold])
        fish_list.append(fish_hold)
    retval_list = []
    for val in (fish_list):
        retval_list.append(val.replace('||', '|'))
    return '\n'.join(retval_list)
