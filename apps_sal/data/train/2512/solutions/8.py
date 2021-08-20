class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        tmp = set()
        for email in emails:
            (local_name, domain_name) = email.split('@')
            before_first_plus = local_name.split('+')[0]
            without_dot_list = before_first_plus.split('.')
            final_local_name = ''.join(without_dot_list)
            tmp.add(final_local_name + '@' + domain_name)
        return len(tmp)
