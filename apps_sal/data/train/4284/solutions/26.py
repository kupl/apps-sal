def array_leaders(numbers):
    i = 0
    output = []
    for num in numbers:
        sum_right = sum(numbers[i + 1:len(numbers)])
        if sum_right < num:
            output.append(num)
        else:
            pass
        i += 1
    return output
