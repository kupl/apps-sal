class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        l = []
        for i in emails:
            end = i[i.index('@'):]
            s = ''
            string = ''
            for j in i:
                if j == '.':
                    continue
                if j == '+':
                    break
                if j == '@':
                    break
                else:
                    s = s + j
            l.append(s + end)
        return len(set(l))
