def increment_string(strng):
    if strng=='': # To ensure there aren't any index errors.
        return '1'
    if strng[-1] not in ['0','1','2','3','4','5','6','7','8','9']:
        return strng+'1' # To add a '1' at the end of any string without numbers at the end.
    numChar=1 # numChar is the number of characters that are numbers at the end of strng.
    try:
        while True:
            if strng[-numChar] in ['0','1','2','3','4','5','6','7','8','9']:
                numChar+=1
            else:
                break
    except:
        numChar=len(strng)
    strngNum=strng[-numChar+1:]
    finalNum=str(int(strngNum)+1)
    while len(strngNum)>len(finalNum): # This is to ensure there are the correct number of 0s.
        finalNum='0'+finalNum
    return strng[:-numChar+1]+finalNum
