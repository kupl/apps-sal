class Solution:
\tdef longestAwesome(self, s: str) -> int:
\t\tseen = {0: -1}
\t\tcurrent_xor = 0
\t\tanswer = 1
\t\tn = len(s)
\t\txor_list = {0: 1, 1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512}
\t\tfor i in range(n):
\t\t\tcurrent_xor ^= xor_list[int(s[i])]
\t\t\tif current_xor not in seen:
\t\t\t\tseen[current_xor] = i
\t\t\telse:
\t\t\t\tanswer = max(answer, i - seen[current_xor])
\t\t\tfor j in range(10):
\t\t\t\tnew_xor = current_xor ^ xor_list[j]
\t\t\t\tif new_xor in seen:
\t\t\t\t\tanswer = max(answer, i - seen[new_xor])
\t\treturn answer
