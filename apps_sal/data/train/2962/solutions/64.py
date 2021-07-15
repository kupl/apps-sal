def divisible_by(numbers, divisor):
    liste = []
    for i in range(0,len(numbers)):
        if numbers[i] % divisor == 0:
            liste.append(numbers[i])
            i += 1
    return liste
