def middle_permutation(string):
    sortedString = ''.join(sorted(string))
    reversedString = sortedString[::-1]
    result = ''
    result += reversedString[int(len(reversedString)/2) : int((len(reversedString)+3)/2)]
    result += reversedString[0:int(len(reversedString)/2)]
    result += reversedString[int((len(reversedString)+3)/2):]
    return result
