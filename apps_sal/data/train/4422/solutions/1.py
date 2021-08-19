# Kata: String -> N iterations -> String  Rating 5kyu


# To optimize this problem, we must look at the circular (modular) nature of the iterations
# of the even/odd rule.  Given any string, under the even/odd rule, the number of permutations
# will be no longer than the length of the original message.
# e.g. 'abcdefghijklmnop' has only four unique permutations under the even/odd rule:
#      ['abcdefghijklmnop', 'acegikmobdfhjlnp', 'aeimbfjncgkodhlp', 'aibjckdlemfngohp']
# So, if we want to apply the even/odd rule N times for string 'abcdefghijklmnop', we need but
# access the 'N modulo n' element in the permutation list (where m is the length of permutation list)


def buildPermList(originalMsg):

    listPerms = []
    listPerms.append(originalMsg)  # index 0 is original message
    curMsg = originalMsg

    while True:
        even = curMsg[0::2]
        odd = curMsg[1::2]
        curMsg = even + odd
        if curMsg != originalMsg:  # Scenario: Back to the original message
            listPerms.append(curMsg)
        else:
            break

    # listPerms is <= the length of the origianl message; ith element is the ith permutation under
    # the even/odd rules
    return listPerms
# -----end function


def jumbled_string(msg, n):

    permList = buildPermList(msg)
    numUniquePerms = len(permList)
    desiredRotIndex = n % numUniquePerms

    return permList[desiredRotIndex]

# -----end function


# Demonstrative test code
# msg = 'abcdefghijklmnop'
# n=18
# myList = buildPermList(msg)
# print("---Length of list: ", len(myList))
# print("---List: ", myList)
# lenList = len(myList)
# desiredIndex = n % lenList
# print( "The location: ", str(desiredIndex) )
# print( "Desired String",  rotationsByN(msg, n) )
