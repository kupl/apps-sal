def disarium_number(number):
    m = 10
    i = 10
    result = 0
    count = 1
    once = True
    a = None
    zero_count = 0
    while count > 0:
        # get the length of the number 
        if int(number/i) != 0:
            # if the number ends by zeros remove them store the answer in a
            # count number of zeros
            if number % i == 0:
                a = int(number /i)
                zero_count += 1
            i *= 10
            count += 1
        else:
        # if a exists means number have zeros so we change it from number to a so that it can be operated as other numbers
        # also i will change from 10 power whole length of number to 10 power length of a
            if a is not None:
                                number = a
                                count = count - zero_count
                                i = 10 ** count
            j = count
            for q in range(j+1):
            # get numbers by each iteration power them their position add those powers to result
            # once will help to check if the last number is still the same after getting it from the whole number
                k = (number * (m ** count))/ i
                p = int(((k/10)%1) * 10)
                if once and number % 2 != p % 2:
                    p += 1
                    once = False
                once = False
                result += p ** count
                count -= 1
                if count < 1:
                    break
    if number == result:
        return "Disarium !!"
    return "Not !!"

