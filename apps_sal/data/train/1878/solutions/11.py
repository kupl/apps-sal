class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict = {}
        sortedArr = sorted(arr)
        for i in range(len(sortedArr)):
            if(sortedArr[i] not in dict):
                dict[sortedArr[i]] = [i]
            else:
                dict[sortedArr[i]].append(i)

        position = []
        for i, val in enumerate(arr):
            position.append(dict[val][0] - i)
            dict[val].pop(0)

        maxNum = 0
        i = 0
        ifPlusMinus = 0
        maxIdealPosition = 0
        while(i < len(position)):
            if(position[i] == 0 and ifPlusMinus == 0):
                maxNum += 1
                i += 1
            elif(position[i] > 0 and ifPlusMinus == 0):
                ifPlusMinus = 1
                maxIdealPosition = i + position[i]
                i += 1
            elif(position[i] >= 0 and ifPlusMinus == 1):
                if(i + position[i] > maxIdealPosition):
                    maxIdealPosition = i + position[i]
                i += 1
            elif(position[i] < 0 and ifPlusMinus == 1):
                if(i < len(position) - 1):
                    if(position[i + 1] < 0):
                        i += 1
                    elif(position[i + 1] >= 0):
                        if(i == maxIdealPosition):
                            maxNum += 1
                            ifPlusMinus = 0
                            maxIdealPosition = 0
                        i += 1
                else:
                    maxNum += 1
                    ifPlusMinus = 0
                    i += 1

        return maxNum
