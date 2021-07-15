def solve(s):
    max = num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
            if max < num:
                max = num
        else:
            num = 0
    
    return max
