class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        dic = {}
        list = []
        list2 = []
        number = 0
        # set a dictionary, 1~26 related a~z
        for letter in string.ascii_lowercase:
            dic[letter] = number + 1
            number = number + 1
        # calculate the difference between the two letter, if the target over the letter, put it into list, otherwise put it into list2
        for element in letters:
            if dic[element] > dic[target]:
                list.append(dic[element] - dic[target])
            else:
                list2.append(dic[element])
        # find the difference and calculate the nearest letter
        if list != []:
            minnum = min(list)
            return string.ascii_lowercase[dic[target] + minnum - 1]
        else:
            minnum = min(list2)
            return string.ascii_lowercase[minnum - 1]
