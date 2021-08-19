def solve(s):
    largest = 0
    number = 0
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
            if largest < number:
                largest = number
        else:
            number = 0
    return largest
