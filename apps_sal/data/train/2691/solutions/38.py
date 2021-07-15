def solve(s):
    max_int = -1
    current_num = ''
    for char in s:
        if char in '0123456789':
            current_num += char
            max_int = max(max_int, int(current_num))
        else:
            current_num = ''
    return max_int
