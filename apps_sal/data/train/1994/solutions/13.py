from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class UF:
    def __init__(self):
        self.p = {}
        self.r = defaultdict(lambda: 1)
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.r[x] > self.r[y]:
            self.p[y] = x
        elif self.r[x] < self.r[y]:
            self.p[x] = y
        else:
            self.p[x] = y
            self.r[y] += 1
    
    def find(self, x):
        if self.p.get(x, x) != x:
            self.p[x] = self.find(self.p.get(x,x))
        return self.p.get(x, x)

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        uf = UF()
        # uf.union(head.val, head.next.val)
        # return 0 
        gSet = set(G)
        prev = head.val
        head = head.next
        # print(\"AB\")
        while head != None:
        # for i in range(1):
            # print
            curr = head.val
            if curr in gSet and prev in gSet:
                uf.union(curr, prev)
                # return 1
            head = head.next
            prev = curr
        # return 0  
        resSet = set()
        # print(G[1])
        # print(uf.p)
        # resSet.add(uf.find(i))
        # resSet.add(uf.find(G[1]))
        # return 10
        for i in G:
            # print(i)
            resSet.add(uf.find(i))
        # print(resSet, uf.p)
        return len(resSet)
