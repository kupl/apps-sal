def solve(s):
    substr = ""
    sub_list = []
    prev_digit = s[0].isdigit()
    
    for char in s:
        this_digit = char.isdigit()
        if this_digit != prev_digit:
            sub_list.append(substr)
            substr = ""
            prev_digit = this_digit
    
        substr += char

    sub_list.append(substr)

    list_of_numbers = []
    
    final_list = [s for s in sub_list if s.isdigit()]
    
    high = max(map(int,final_list))
    
    return high
