import math
import collections


def getAllPrimeFactors(n):
    if isinstance(n, int) and n > -1:
        if n != 1:
            listy, m, x = [], n, True
            while x:
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        n = n // i
                        listy.append(i)
                        break
                else:
                    x = False
            if m > 1:
                listy.append(n)
            return listy
        else:
            return [1]
    else:
        return []


def getUniquePrimeFactorsWithCount(n):
    if isinstance(n, int) and n > -1:
        if n != 1:
            listy, m, x = [], n, True
            while x:
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        n = n // i
                        listy.append(i)
                        break
                else:
                    x = False
            if m > 1:
                listy.append(n)
        else:
            listy = [1]
    else:
        listy = []
    fancy_dict = collections.Counter()
    resulty_list = [[], []]
    for number in listy:
        fancy_dict[number] += 1
    for key, value in list(fancy_dict.items()):
        resulty_list[0].append(key)
        resulty_list[1].append(value)
    return resulty_list


def getUniquePrimeFactorsWithProducts(n):
    if isinstance(n, int) and n > -1:
        if n != 1:
            listy, m, x = [], n, True
            while x:
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        n = n // i
                        listy.append(i)
                        break
                else:
                    x = False
            if m > 1:
                listy.append(n)
        else:
            listy = [1]
    else:
        listy = []
    fancy_dict = collections.Counter()
    resulty_list = [[], []]
    for number in listy:
        fancy_dict[number] += 1
    for key, value in list(fancy_dict.items()):
        resulty_list[0].append(key)
        resulty_list[1].append(value)
    return [resulty_list[0][i]**resulty_list[1][i] for i in range(len(resulty_list[0]))]
