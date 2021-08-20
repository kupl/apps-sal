class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        t = head
        temp = []
        while t:
            temp.append(t.val)
            t = t.next
        (stack, result) = ([0], [])
        for i in range(1, len(temp)):
            if temp[i] > temp[stack[-1]]:
                result.append(temp[i])
                stack.pop()
                while stack:
                    if temp[i] > temp[stack[-1]]:
                        result[stack[-1]] = temp[i]
                        stack.pop()
                    else:
                        break
                stack.append(i)
            else:
                stack.append(i)
                result.append(0)
        result.append(0)
        return result
