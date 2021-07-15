def solve(s):
    max_num = float('-inf')
    temp = ''
    
    for i in s:
        if i.isdigit():
            temp += i
            max_num = max(max_num, int(temp))
        else:
            temp = ''
            
    return max_num
