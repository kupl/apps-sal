class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        temp = head
        array = self.createArray(temp)
        curSum = 0
        index = 0
        while index < len(array):
            for i in range(index, len(array)):
                curSum += array[i]
                if curSum == 0:
                    self.clearOutArray(array, index, i)
                    index = i + 1
                    curSum = 0
            curSum = 0
            index += 1
        finalArray = []
        for num in array:
            if num != None:
                finalArray.append(num)
        newNode = self.create(finalArray)
        return newNode

    def clearOutArray(self, array, index, i):
        for i in range(index, i + 1):
            array[i] = None
        return

    def create(self, array):
        if len(array) == 0:
            return None
        else:
            node = ListNode(array[0])
            temp = node
            for i in range(1, len(array)):
                node.next = ListNode(array[i])
                node = node.__next__
            node.next = None
        return temp

    def createArray(self, temp):
        array = []
        while temp != None:
            array.append(temp.val)
            temp = temp.__next__
        return array
