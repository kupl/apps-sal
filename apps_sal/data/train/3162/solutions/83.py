def compare(s1, s2):

    sumOne = 0
    sumTwo = 0

    if s1 != None:
        if s1.isalpha():
            s1 = s1.upper()
            sumOne = sum([ord(char) for char in s1])
    if s1 != None:
        if s2.isalpha():
            s2 = s2.upper()
            sumTwo = sum([ord(char) for char in s2])

    if sumOne == sumTwo:
        return True
    else:
        return False
