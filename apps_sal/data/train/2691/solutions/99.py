def solve(s):
    numbers = []
    temp = ''
    for char in s:
        if char.isnumeric():
            temp += char
            numbers.append(int(temp))
        else:
            try:
                numbers.append(int(temp))
                temp = ''
            except:
                continue        
    return max(numbers)
