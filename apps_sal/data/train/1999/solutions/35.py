# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        
        array = []
        modified = False
        node = head
        #print(\"Head: \", head)
        while node:
            #print(\"node: \", node.val, modified, matched)
            next_node = node.__next__
            matched = False
            if node.val == 0:
                matched = True
                modified = True
                if len(array) > 0:
                    array[-1].next = next_node
                else:
                    head = next_node
            
            else:
                tsum = 0
                #print(\"For: \", node.val)
                for i in range(len(array) -1, -1, -1):
                    tsum += array[i].val
                    if tsum + node.val == 0:
                        matched = True
                        modified = True
                        #print(i)
                        if i != 0:
                            j = 0
                            popi = len(array) - i
                            while j != popi:
                                array.pop()
                                j += 1
                            array[i-1].next = next_node
                            #print(array[i-1].val, next_node.val, head)
                        else:
                            # all elements removed
                            head = next_node
                            array = []
                    # elif tsum + node.val > 0:
                    #     break
                        
            if not matched:
                array.append(node)
            node = next_node
        #print(\"op head: \", head)
        if modified:
            return self.removeZeroSumSublists(head)
        else:
            return head        
        

