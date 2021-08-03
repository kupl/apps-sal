def array_leaders(numbers):
    count, res = 0, []
    while count < len(numbers):
        if len(numbers[count + 1:]) >= 0:
            if numbers[count] > sum(numbers[count + 1:]):
                print(numbers[count])
                res.append(numbers[count])
        count += 1
    return res
