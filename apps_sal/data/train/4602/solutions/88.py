# write the function is_anagram
def is_anagram(test, original):
    theTest = test.lower()
    theOriginal= original.lower()
    if len(theTest) != len(theOriginal):
        return False
    else:
        index = 0
        lengthCheck = 0
        array = [None] * len(theTest)
        for i in theOriginal:
            array[index] = i
            index += 1
        for j in theTest:
            testLength = len(theTest)
            if j in array:
                lengthCheck += 1
            else:
                return False
        if lengthCheck == testLength:
            return True

