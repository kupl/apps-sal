def solve(s):
    str_num = ""
    num_fin = 0 
    j_count = 0 
    len_s = len(s)
    for a in s :
        if a.isdigit() :
            str_num = str_num + a
            
        if ((not a.isdigit()) or j_count==(len_s - 1)) and str_num != '' :
            
            num_fin = max(int(str_num),num_fin)
            str_num = ""
        j_count = j_count + 1     
    return num_fin
