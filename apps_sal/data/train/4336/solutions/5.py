def mem_alloc(block):
    common_set = set()
    new_list = tuple(block)
    while not(new_list in common_set):
        common_set.add(new_list)
        new_list = list(new_list)
        max_num = max(new_list)
        len_list = len(new_list)
        base_num, len_mod_num = divmod(max_num, len_list)
        len_div_num = len_list - len_mod_num
        ind = new_list.index(max_num)
        new_list[ind] = 0
        
        pattern_num = [base_num] * len_div_num + [base_num + 1] * len_mod_num
        pattern_num = pattern_num[ind::-1] + pattern_num[len_list:ind:-1]
        for i in range(len_list): new_list[i] += pattern_num[i]
        new_list = tuple(new_list)
    return len(common_set)
