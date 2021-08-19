def increment_string(strng):
    if strng == '':
        return '1'
    if strng[-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return strng + '1'
    numChar = 1
    try:
        while True:
            if strng[-numChar] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                numChar += 1
            else:
                break
    except:
        numChar = len(strng)
    strngNum = strng[-numChar + 1:]
    finalNum = str(int(strngNum) + 1)
    while len(strngNum) > len(finalNum):
        finalNum = '0' + finalNum
    return strng[:-numChar + 1] + finalNum
