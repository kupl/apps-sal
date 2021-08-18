class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        result = 0
        node = head
        tmp = []
        while node is not None:
            if node.val in G:
                tmp.append(node.val)
                node = node.next
            else:
                if tmp:
                    result += 1
                    tmp = []
                node = node.next
        if tmp:
            result += 1
        return result
