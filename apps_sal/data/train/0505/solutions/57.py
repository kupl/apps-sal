from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def process_s(s):
            chs = deque([])
            opening_p_count = 0
            for ch in s:
                if ch == '(':
                    opening_p_count += 1
                elif ch == ')':
                    if opening_p_count == 0:
                        continue
                    opening_p_count -= 1
                chs.append(ch)
                
            final_chs = deque([])
            closing_p_count = 0
            for i in range(len(chs) - 1, -1, -1):
                ch = chs[i]
                if ch == '(':
                    if closing_p_count == 0:
                        continue
                    closing_p_count -= 1
                elif ch == ')':
                    closing_p_count += 1
                final_chs.appendleft(ch)
                
            return ''.join(final_chs)
                        
        return process_s(s)

