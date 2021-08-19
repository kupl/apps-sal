class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        index_to_remove = set()
        for (index, item) in enumerate(s):
            if item == '(':
                stack.append(index)
            elif item == ')':
                if not stack:
                    index_to_remove.add(index)
                else:
                    stack.pop()
        print(stack)
        print(index_to_remove)
        string_builder = []
        for (index, item) in enumerate(s):
            if index not in stack and index not in index_to_remove:
                string_builder.append(item)
        return ''.join(string_builder)
