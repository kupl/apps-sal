class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next

        count = 0
        i = 0
        flag = 0
        while i < len(lst):
            if lst[i] in G:
                i = i + 1
                flag = 1
                continue
            elif flag == 1 and lst[i] not in G:
                count = count + 1
                i = i + 1
                flag = 0
            else:
                i = i + 1

        if lst[-1] in G:
            count = count + 1
        return count
