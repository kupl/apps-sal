def isprime(x):
    number = x
    if number == 2:
        return True
    else:
        for num in range(2, number):
            if number % num == 0:
                return False
        else:
            return True


def num_primorial(num_of_nums):
    counter = 0
    number = 2
    primorial = 1
    for x in range(2, 10000):
        if isprime(number) == True:
            primorial *= x
            number += 1
            counter += 1
            if counter == num_of_nums:
                break
        else:
            number += 1
    return primorial
