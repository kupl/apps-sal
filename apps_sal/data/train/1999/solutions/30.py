# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.__next__
        D = [0]*(len(arr)+1)
        for i in range(1,len(D)):
            D[i] = D[i-1] + arr[i-1]
        
        tmp_dict = {}
        for i in range(len(D)):
            if D[i] not in tmp_dict:
                tmp_dict[D[i]] = [i]
            else:
                tmp_dict[D[i]].append(i)
        i = 0
        remove = []
        while i<len(D):
            if len(tmp_dict[D[i]])>1:
                if i!=tmp_dict[D[i]][-1]:
                    remove.append([i,tmp_dict[D[i]][-1]])
                i = tmp_dict[D[i]][-1] + 1
            else:
                i += 1
        
        remove_idx = []
        for i in range(len(remove)):
            remove_idx += [e for e in range(remove[i][0],remove[i][1])]
        
        res = []
        for i in range(len(arr)):
            if i not in remove_idx:
                res.append(arr[i])
        
        if len(res)==0:
            return None
        else:
            head = ListNode(res[0])
            pre = head
            for i in range(1,len(res)):
                node = ListNode(res[i])
                pre.next = node
                pre = node
            return head
                

