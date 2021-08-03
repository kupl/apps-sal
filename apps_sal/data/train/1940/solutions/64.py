class Stack:
    def __init__(self):
        self.items = []
        self.time_stamps = dict()
        self.t = 0

    def isEmpty(self):
        return self.items == []

    def push(self, item):

        self.items.append([item, self.t])
        self.time_stamps[item] = self.t
        self.t += 1

    def pop(self):
        return self.items.pop()

    def peek1(self):
        return self.items[len(self.items) - 1][0]

    def peek2(self):
        return self.items[len(self.items) - 1][1]

    def size(self):
        return len(self.items)

    def ret(self):
        return self.items


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        T = []
        while head:
            T.append(head.val)
            head = head.__next__

        def dailyTemperatures(T: List[int]) -> List[int]:
            if len(T) == 0:
                return [0]
            ans = [0] * len(T)
            stack = Stack()
            stack.push(T[0])

            for i in range(1, len(T)):
                current = T[i]
                if current <= stack.peek1():
                    stack.push(current)

                else:
                    while(stack.size() != 0 and current > stack.peek1()):
                        ans[stack.peek2()] = stack.t - stack.peek2()
                        stack.pop()
                    stack.push(current)

            return ans
        S = dailyTemperatures(T)
        n = len(S)
        ans = [0] * n
        for i in range(n):
            if S[i] != 0:
                ans[i] = T[i + S[i]]

        return ans
