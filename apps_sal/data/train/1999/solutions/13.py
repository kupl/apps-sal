# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if(head is None):
            return None
        temp = head
        array = self.createArray(temp)
        curSum = 0
        index = 0
        while(index < len(array)):
            for i in range(index, len(array)):
                curSum += array[i]
                if(curSum == 0):
                    self.clearOutArray(array, index, i)
                    index = i + 1
                    curSum = 0
            curSum = 0
            index += 1

        newNode = self.create(array)
        return newNode

    def clearOutArray(self, array, index, i):
        for i in range(index, i + 1):
            array[i] = None
        return

    def create(self, array):
        if(len(array) == 0):
            return None
        node = None
        temp = None
        for i in range(0, len(array)):
            if(array[i] != None):
                if(node is None):
                    node = ListNode(array[i])
                    temp = node
                else:
                    node.next = ListNode(array[i])
                    node = node.__next__
        if(node is not None):
            node.next = None
        return temp

    def createArray(self, temp):
        array = []
        while(temp != None):
            array.append(temp.val)
            temp = temp.__next__
        return array
