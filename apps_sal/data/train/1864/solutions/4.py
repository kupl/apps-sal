class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        for letter in expression:
            if letter.isalpha():
                stack.append(set(letter))
            elif letter == '{':
                stack.append('{')
            elif letter == ',':
                stack.append(',')
            elif letter == '}':
                while stack[-2] == ',':
                    set2 = stack.pop()
                    stack.pop()
                    stack[-1].update(set2)
                tail = stack.pop()
                stack[-1] = tail
            while len(stack) > 1 and isinstance(stack[-1], set) and isinstance(stack[-2], set):
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set(w1 + w2 for w1 in set1 for w2 in set2))

        return list(sorted(stack[-1]))
