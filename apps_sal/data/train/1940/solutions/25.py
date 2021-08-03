# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        aux = Stack()
        result = []

        current = head

        i = 0
        while current:
            result.append(0)
            if aux.is_empty() or aux.peek()[1] >= current.val:
                aux.push((i, current.val))
                current = current.next
                i += 1
                continue

            while (not aux.is_empty()) and (aux.peek()[1] < current.val):
                position, value = aux.pop()
                result[position] = current.val
            aux.push((i, current.val))
            i += 1
            current = current.next
        return result
