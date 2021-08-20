def solve(s):
    string = ''
    for (i, item) in enumerate(s):
        if item.isalpha():
            string += ' '
        else:
            string += item
    numbers = string.split()
    numbers = [int(i) for i in numbers]
    return max(numbers)
