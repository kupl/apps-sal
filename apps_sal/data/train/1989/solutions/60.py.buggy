class Solution:
\tdef longestAwesome(self, s: str) -> int:
\t\tseen = {0: -1}
\t\tcurrent_xor = 0
\t\tanswer = 1
\t\tn = len(s)
\t\tfor i in range(n):
\t\t\tcurrent_xor ^= 1 << int(s[i])
\t\t\tif current_xor not in seen:
\t\t\t\tseen[current_xor] = i
\t\t\telse:
\t\t\t\tanswer = max(answer, i - seen[current_xor])
\t\t\tfor j in range(10):
\t\t\t\tnew_xor = current_xor ^ (1 << j)
\t\t\t\tif new_xor in seen:
\t\t\t\t\tanswer = max(answer, i - seen[new_xor])
\t\treturn answer
