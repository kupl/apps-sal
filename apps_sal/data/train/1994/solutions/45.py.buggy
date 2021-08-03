# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        normal_list = []
        while head:
            normal_list.append(head.val)
            head = head.next
            
        print(\"normal_list: \", normal_list)
        
        G.sort()
        print(\"G: \", G)
        
        groups = 0
        stack = []
        group_started = False
        
        # traverse normal_list
        while len(normal_list) > 0:
            a = normal_list.pop(0)
            if a in G:
                group_started = True
            else:
                if group_started == True:
                    groups += 1
                    group_started = False
        
        if group_started == True:
            groups += 1
        
        return groups
            
        
#         i = 0
#         while i < len(normal_list):
#             while i < len(normal_list) and normal_list[i] != G[i]:
#                 G.insert(i, \"\")
#                 i+=1
            
#             i+=1
            
#         print(\"G: \", G)
        
#         groups = 0
        
#         g = 0
#         groups_started = False
#         while g < len(G):
#             if G[g] != '':
#                 groups_started = True
#             else:
#                 if groups_started == True:
#                     groups += 1
#                     groups_started = False
#             g+=1
        
#         if groups_started == True:
#             groups +=1 # for the last one
        
#         print(\"groups: \", groups)
#         return groups
        
        
        
