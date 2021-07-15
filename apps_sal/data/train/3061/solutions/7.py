def getNumAndFreq(myList):
    curNum = myList.pop(0)
    freqCurNum = 1
    while myList and  myList[0] == curNum:
        myList.pop(0)
        freqCurNum +=1

    return curNum, freqCurNum
#---end function getNumAndFreq


def most_frequent_item_count( myList ):

    myList.sort()

    maxNum = 0
    maxFreq = 0
    while myList:
        curNum, curFreq = getNumAndFreq(myList)
        if maxFreq < curFreq:
            maxNum = curNum; maxFreq = curFreq

    #return maxNum, maxFreq     #if you want num with max freq
    return maxFreq

#-----end fucntion

