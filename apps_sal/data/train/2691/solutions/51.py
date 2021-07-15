def solve(s):
    import re
    
    numbers = re.findall(r"\d+",s)
    int_numbers = [int(i) for i in numbers]
    return max(int_numbers)
