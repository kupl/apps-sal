class Solution:

    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        prev = set()
        curr = set()
        for s in expression:
            if s == '{':
                stack.append(prev)
                stack.append(curr)
                curr = set()
                prev = set()
            elif s == '}':
                k = stack.pop()
                p = set()
                for i in k or ['']:
                    for j in prev | curr:
                        p.add(i + j)
                prev = stack.pop()
                curr = p
            elif s == ',':
                prev |= curr
                curr = set()
            else:
                p = set()
                for c in curr or ['']:
                    p.add(c + s)
                curr = p
        return list(sorted(curr))
