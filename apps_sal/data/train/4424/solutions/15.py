def expression_matter(a, b, c):
    numbers = [a, b, c]

    total = 0
    iCount = 0

    ttl2 = 0
    if 1 in numbers:
        iCount = numbers.count(1)

        for i in numbers:
            if(iCount == 1):
                if(numbers[1] == 1):
                    if(numbers[0] == max(numbers)): ttl2 = 1
                    if(numbers.count(max(numbers)) == 2):
                        ttl2 += i
                    else:
                        if(i != max(numbers)):
                            ttl2 += i
                    total = ttl2 * max(numbers)
                elif(numbers[0] == 1):
                    ttl2 = numbers[0] + numbers[1]
                    total = ttl2 * numbers[2]
                elif(numbers[2] == 1):
                    ttl2 = numbers[2] + numbers[1]
                    total = ttl2 * numbers[0]
            elif(iCount == 2):
                if(numbers[0] == numbers[1] or numbers[1] == numbers[2]):
                    total = max(numbers) * 2
                else:
                    total += i
            elif(iCount == 3):
                total += i
            else:
                if(i == max(numbers)):
                    if(numbers[0] == max(numbers)): total = 1
                    total *= i
                else:
                    total += i
    else:
        total = 1
        for i in numbers:
            total *= i

    return(total)
