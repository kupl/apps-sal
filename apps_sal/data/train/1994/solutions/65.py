class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr_node = head
        value_in = False
        no = 0
        while curr_node:
            if curr_node.val in G:
                value_in = True
            else:
                if value_in:
                    no = no + 1
                    value_in = False
            curr_node = curr_node.__next__
        if value_in:
            no = no + 1
        return no
