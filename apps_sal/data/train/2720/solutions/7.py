def solution(digits):
    final = 0
    stg = str(digits)
    for (num1, num2) in enumerate(stg):
        try:
            if int(str(stg[num1]) + str(stg[num1 + 1])) > final:
                final = int(str(stg[num1]) + str(stg[num1 + 1]))
            if int(str(stg[num1]) + str(stg[num1 + 1]) + str(stg[num1 + 2])) > final:
                final = int(str(stg[num1]) + str(stg[num1 + 1]) + str(stg[num1 + 2]))
            if int(str(stg[num1]) + str(stg[num1 + 1]) + str(stg[num1 + 2]) + str(stg[num1 + 3])) > final:
                final = int(str(stg[num1]) + str(stg[num1 + 1]) + str(stg[num1 + 2]) + str(stg[num1 + 3]))
            if int(str(stg[num1]) + str(stg[num1 + 1]) + str(stg[num1 + 2]) + str(stg[num1 + 3]) + str(stg[num1 + 4])) > final:
                final = int(str(stg[num1]) + str(stg[num1 + 1]) + str(stg[num1 + 2]) + str(stg[num1 + 3]) + str(stg[num1 + 4]))

        except:
            pass
    return final
