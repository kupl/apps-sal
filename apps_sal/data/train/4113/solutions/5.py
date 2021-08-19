def solution(number):
    returnArray = [0, 0, 0]
    for i in range(1, number):
        if i % 15 == 0:
            returnArray[2] += 1
        elif i % 5 == 0 and (not i % 3 == 0):
            returnArray[1] += 1
        elif i % 3 == 0:
            returnArray[0] += 1
    return returnArray
