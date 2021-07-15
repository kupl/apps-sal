# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        memo = {}
        t=head
        nodes=[]
        while t:
            nodes.append(t.val)
            t=t.__next__
        
        maxes = [0]*len(nodes)
        sol = [0]*len(nodes)
        for idx,val in enumerate(nodes[::-1]):
            if idx != 0:
                maxes[-idx-1] = max(maxes[-idx],nodes[-idx])
            else:
                maxes[-idx-1] = nodes[-idx-1]
                
        for idx,val in enumerate(nodes):
            if val in memo and memo[val] > idx:
                sol[idx] = nodes[memo[val]]
            elif maxes[idx] > val:
                for j in range(idx+1,len(nodes)):
                    if nodes[j]>val:
                        memo[val] = j
                        sol[idx] = nodes[j]
                        break
            else:
                continue
        
        return sol

