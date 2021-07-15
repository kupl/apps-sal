class Solution:
    def removeDuplicates(self, S: str) -> str:
        cur = list(S)
        while True:
            next_l = []
            i = 0
            while i < len(cur):
                if i < len(cur) - 1 and cur[i] == cur[i + 1]:
                    i += 2
                    continue
                next_l.append(cur[i])
                i += 1
            if len(next_l) == len(cur):
                return ''.join(next_l)
            cur = next_l
        
        return ''

