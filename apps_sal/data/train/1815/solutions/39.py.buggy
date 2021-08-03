class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
#         output = list(S)
#         if len(S) == 0 or len(S) != len(shifts): return output
#         alphabet = \"abcdefghijklmnopqrstuvwxyz\"
#         for i, k in enumerate(shifts):
#             # shifting logic and make dict
#             cipherString = alphabet[k%len(alphabet):] + alphabet[:k%len(alphabet)]
#             cipher = dict(zip(alphabet, cipherString))
#             for j in range(i + 1):
#                 # add to output
#                 output[j] = cipher[output[j]]
            
#         return ''.join(output)

        output = list(S)
        if len(S) == 0 or len(S) != len(shifts): return output
        alphabet = \"abcdefghijklmnopqrstuvwxyz\"
        shift = sum(shifts)
        for i, l in enumerate(S):
            cipherString = alphabet[shift%len(alphabet):] + alphabet[:shift%len(alphabet)]
            cipher = dict(zip(alphabet, cipherString))
            output[i] = cipher[l]
            shift -= shifts[i]
            
        return ''.join(output)
            
        
