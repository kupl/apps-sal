def tidyNumber(n):
    numbers = [int(num) for num in str(n)]

    # assume tidy until proven otherwise
    flag = True

    while len(numbers) > 1:
        if numbers[0] > numbers[1]:  # check counter-condition for each
            flag = False            # if satisfies, not tidy
            break                   # escape loop
        numbers.pop(0)              # else, remove first element and iterate
    return flag
