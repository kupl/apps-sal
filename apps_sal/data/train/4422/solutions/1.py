

def buildPermList(originalMsg):

    listPerms = []
    listPerms.append(originalMsg)
    curMsg = originalMsg

    while True:
        even = curMsg[0::2]
        odd = curMsg[1::2]
        curMsg = even + odd
        if curMsg != originalMsg:
            listPerms.append(curMsg)
        else:
            break

    return listPerms


def jumbled_string(msg, n):

    permList = buildPermList(msg)
    numUniquePerms = len(permList)
    desiredRotIndex = n % numUniquePerms

    return permList[desiredRotIndex]
