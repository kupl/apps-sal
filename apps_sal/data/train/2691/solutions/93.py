def solve(s):
    next_number = 0
    largest_number = 0
    for char in s:
        if str.isnumeric(char):
            next_number = int(str(next_number) + str(char))
        else:
            if next_number > largest_number:
                largest_number = next_number
            next_number = 0

    if next_number > largest_number:
        largest_number = next_number
    return largest_number


print(solve('lu1j8qbbb85'))
