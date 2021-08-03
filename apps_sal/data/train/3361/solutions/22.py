def sum_of_minimums(numbers):
    output = 0
    for row in numbers:
        row.sort()
        output += row[0]
    return output
