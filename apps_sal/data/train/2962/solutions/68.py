def divisible_by(numbers, divisor):
    divList = []
    for i in range(len(numbers)): 
        if numbers[i] % divisor == 0: 
            divList.append(numbers[i])
    return divList
