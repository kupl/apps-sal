def sort_it(list_, n):    
    str_list = list_.split(", ")
    str_list.sort(key=lambda f: f[n - 1])
    return ", " .join(str_list)
