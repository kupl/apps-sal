# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        temp=[]
        i=head
        while i!=None:
            temp.append(i.val)
            i=i.next
        #print(temp)
        n=len(temp)
        res=[0]*n
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if(temp[j]>temp[i]):
                    res[i]=temp[j]
                    break
                elif((temp[j]==temp[i])or(res[j]==0)):
                    res[i]=res[j]
                    break
        return res
