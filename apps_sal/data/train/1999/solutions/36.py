class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr = head
        while curr is not None and curr.val == 0:
            curr = curr.__next__
        dummy = ListNode(0, curr)
        if curr is not None:
            memo = [[dummy], [curr, curr.val]]
        curr = curr.__next__ if curr is not None else None
        while curr is not None:
            last_index = len(memo) - 1
            if curr.val == 0:
                memo[last_index][0].next = curr.__next__
                curr = curr.__next__
                continue
            curr_list = [curr]
            flag = True
            for i in range(1, len(memo[last_index])):
                val = memo[last_index][i] + curr.val
                if val == 0:
                    memo[i - 1][0].next = curr.__next__
                    memo = memo[:i]
                    flag = False
                    break
                else:
                    curr_list.append(val)
            if flag:
                curr_list.append(curr.val)
                memo.append(curr_list)
            curr = curr.__next__
        return dummy.__next__
