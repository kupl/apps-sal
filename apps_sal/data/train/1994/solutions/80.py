class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr_node = head
        value_in = False
        no = 0
        while curr_node:
            if value_in and (not curr_node.val in G):
                no = no + 1
                value_in = False
            elif curr_node.val in G:
                value_in = True
            curr_node = curr_node.__next__
        if value_in:
            no = no + 1
        return no
