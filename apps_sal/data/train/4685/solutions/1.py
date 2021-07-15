def self_descriptive(num):
    numList = list(str(num))
    for i, s in enumerate(numList):
        if int(s) != numList.count(str(i)):
            return False
    return True
