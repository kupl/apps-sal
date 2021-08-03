# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        data = []
        node = head
        maxN = 0
        while node != None:
            data.append(node.val)
            node = node.next
      #  print(data)
        s = []
        out = [0] * len(data)
        for i in range(len(data) - 1, -1, -1):

            while len(s) > 0 and s[-1] <= data[i]:
                s.pop()
            if len(s) > 0:
                out[i] = s[-1]
            s.append(data[i])

        return out
        out = []
        for i in range(len(data) - 1, -1, -1):
         #   print(maxN)

            maxN = max(maxN, data[i])
            if maxN != data[i]:
                out.appendleft(maxN)
            else:
                out.appendleft(0)
          #  print(data[i],maxN)
        return list(out)
        return out
