class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) <= 1:
            return S
        stack = []
        stack.append(S[0])

        index = 1
        while index < len(S):
            stack.append(S[index])
            index += 1

            self.popDups(stack)

        s = ''
        for c in stack:
            s += c

        return s

    def popDups(self, stack):

        to_pop = True
        while stack and to_pop:
            this_item = stack.pop()
            if len(stack) != 0:
                next_item = stack[-1]
                if this_item == next_item:
                    stack.pop()
                else:
                    stack.append(this_item)
                    to_pop = False
            else:
                stack.append(this_item)
                to_pop = False
