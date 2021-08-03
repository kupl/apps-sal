def delete_digit(n):
    numbers = []
    nl = list(str(n))
    for i in range(len(nl)):
        del nl[i]
        number = int("".join(nl))
        numbers.append(number)
        nl = list(str(n))
    numbers.sort()
    numbers = numbers[::-1]
    return numbers[0]
