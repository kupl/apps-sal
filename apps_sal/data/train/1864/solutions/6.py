class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack, cur, prev = [], [], []
        for c in expression:
            if c.isalpha():
                cur = [x + c for x in cur or [\"\"]]
            elif c == ',':
                # Attach cur to prev
                prev += cur
                cur = []
            elif c == '{':
                #print(\"{\", stack, cur, prev)
                stack.append(cur)
                stack.append(prev)
                cur, prev = [], []
            else:
                # Attach cur to prev
                prev += cur
                pre_prev = stack.pop()
                pre_cur = stack.pop()
                # multiply prev and pre_cur
                cur= [p+c for c in prev for p in pre_cur or ['']]
                prev = pre_prev
                #print(\"}\", stack, cur, prev)
        return sorted(set(cur+prev))

