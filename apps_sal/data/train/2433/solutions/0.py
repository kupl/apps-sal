class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
#         count_dash = 0
#         for item in S:
#             if item == '-':
#                 count_dash += 1

#         S_len = len(S) - count_dash

#         ans = ''
#         second_from = 0

#         frist_group = S_len % K
#         if frist_group != 0:
#             count = 0
#             for i in range(len(S)):
#                 if S[i] != '-':
#                     ans = ans + S[i].upper()
#                     count += 1
#                 if count == frist_group:
#                     second_from = i + 1
#                     ans += '-'
#                     break
#         count_k = 0
#         for j in range(second_from,len(S)):
#             if S[j] != '-':
#                 ans = ans + S[j].upper()
#                 count_k += 1
#             if count_k == K:
#                 ans = ans + '-'
#                 count_k = 0

#         return ans[:-1]
        S = S.replace('-', '')[::-1].upper()
        return '-'.join([S[i:i + K] for i in range(0, len(S), K)])[::-1]
