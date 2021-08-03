def min_value(digits):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = []
    for i in numbers:
        if i in digits:
            num.append(i)
    string = ""
    for i in num:
        string += str(i)
    return int(string)
