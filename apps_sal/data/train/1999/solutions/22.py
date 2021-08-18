class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        nodeList = []
        temp = head
        while temp:
            nodeList.append(temp.val)
            temp = temp.next

        x = 0
        while x < len(nodeList):
            y = x
            sum = 0
            while y < len(nodeList):
                sum = sum + nodeList[y]
                if sum == 0:
                    del nodeList[x:y + 1]
                    x -= 1
                    break
                y += 1
            x += 1
        print(nodeList)

        newHead = ListNode()
        currhead = newHead
        for node in nodeList:
            currhead.next = ListNode(node)
            currhead = currhead.next

        return newHead.next
