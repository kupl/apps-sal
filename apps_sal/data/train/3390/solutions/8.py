def narcissistic(value):
    string_of_number = str(value)
    length_of_number = len(string_of_number)
    total = 0
    for i in range(0, length_of_number):
        count = int(string_of_number[i]) ** length_of_number
        total = count + total
    if total == value:
        return True
    else:
        return False
