class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toRemove = []
        output = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if len(toRemove) == 0:
                toRemove.append((c, i))
            elif c == ')' and toRemove[-1][0] == '(':

                toRemove.pop()
            else:
                toRemove.append((c, i))
        s_dict = {i: c for i, c in enumerate(s)}
        for pair in toRemove:
            del s_dict[pair[1]]
        output = [v for k, v in list(s_dict.items())]
        return ''.join(output)
