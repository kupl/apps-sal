class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        prev = None
        currentNode = head
        nextNode = head
        newHead = head
        curSum = 0
        while currentNode != None:
            while nextNode != None:
                curSum += nextNode.val
                if curSum == 0:
                    if prev is None:
                        currentNode = nextNode.__next__
                        newHead = currentNode
                        nextNode = nextNode.__next__
                    else:
                        prev.next = nextNode.__next__
                        currentNode = nextNode.__next__
                        nextNode = nextNode.__next__
                else:
                    nextNode = nextNode.__next__
            curSum = 0
            if currentNode is None:
                break
            prev = currentNode
            currentNode = currentNode.__next__
            nextNode = currentNode
        return newHead
