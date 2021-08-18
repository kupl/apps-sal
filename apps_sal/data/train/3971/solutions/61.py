def tidyNumber(n):
    numbers = [int(num) for num in str(n)]

    flag = True

    while len(numbers) > 1:
        if numbers[0] > numbers[1]:
            flag = False
            break
        numbers.pop(0)
    return flag
