def solve(s):
    number = 0
    largest = 0
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
            if number > largest:
                largest = number
        else: 
            number = 0
            
    return largest

