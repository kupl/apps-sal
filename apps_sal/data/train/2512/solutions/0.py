class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = []
        for email in emails:
            for i in range(len(email)):
                if email[i] == '@':
                    localname = email[:i]
                    domainname = email[i:]
                    local = ''
                    for x in localname:
                        if x == '+':
                            break
                        local += x
                    local = local.replace('.', '')
                    s.append(local + domainname)
                    break
        return len(set(s))
