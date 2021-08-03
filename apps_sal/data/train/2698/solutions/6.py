def sum_arrays(array1, array2):
    if(not array1 and not array2):
        return array1
    elif(not array1):
        return array2
    elif(not array2):
        return array1
    elif(array1 == 0 and array2 == 0):
        nu = []
        return nu

    else:
        nu = []
        if(len(array1) == 1 and len(array2) == 1):
            if(array1[0] == 0 and array2[0] == 0):
                return nu
        print(array1)
        print(array2)
        number1 = 0
        number2 = 0
        num3 = 0
        for x in range(0, len(array1)):
            if(array1[0] < 0):
                if(x == 0):
                    number1 += ((array1[x]) * (10**((len(array1) - 1) - x)))
                else:
                    number1 -= ((array1[x]) * (10**((len(array1) - 1) - x)))
            else:
                number1 += (array1[x] * (10**((len(array1) - 1) - x)))
        for x in range(0, len(array2)):
            if(array2[0] < 0):
                if(x == 0):
                    number2 += ((array2[x]) * (10**((len(array2) - 1) - x)))
                else:
                    number2 -= ((array2[x]) * (10**((len(array2) - 1) - x)))
            else:
                number2 += (array2[x] * (10**((len(array2) - 1) - x)))
        num3 = number1 + number2
        strnum = str(num3)
        answer = []
        if(strnum[0] == 0):
            return nu
        if(strnum[0] == '-'):
            for x in range(1, len(strnum)):
                if(x == 1):
                    answer.append(-1 * int(strnum[x]))
                else:
                    answer.append(int(strnum[x]))
        else:
            for x in range(0, len(strnum)):
                answer.append(int(strnum[x]))
        return answer
