class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = set([])
        for email in emails:
            new_email = ''
            flag = 0
            for i in range(len(email)):
                if email[i] == '.':
                    continue
                if email[i] == '+':
                    flag = 1
                elif email[i] == '@':
                    new_email += email[i:]
                    break
                else:
                    if flag == 0:
                        new_email += email[i]
            dic.add(new_email)
        return len(dic)
