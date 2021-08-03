from collections import defaultdict


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head:
            return 0
        
        temp = head
        prev = None
        adj = defaultdict(list)
        
        while temp:
            adj[temp.val] += [prev.val if prev else None, temp.next.val if temp.next else None]
            prev = temp
            temp = temp.next
        
        \"\"\"exists = defaultdict(bool)
        for g in G:
            exists[g] = True    
        \"\"\"
        visited = defaultdict(bool)
            
        ans = 0
        for g in G:
            if not visited[g]:
                ans += 1
                queue = [g]
                while queue:
                    node = queue[0]
                    queue = queue[1:]
                    visited[node] = True
                    for j in adj[node]:
                        if j is not None and not visited[j] and j in G:
                            queue.append(j)
                            visited[j] = True
                
        return ans
            
            
