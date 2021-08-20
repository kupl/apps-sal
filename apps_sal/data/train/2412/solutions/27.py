class Solution:

    def removeDuplicates(self, S: str) -> str:

        def remove_once(S):
            i = 0
            res = ''
            while i < len(S) - 1:
                if S[i] != S[i + 1]:
                    res += S[i]
                    i += 1
                else:
                    i += 2
            if i == len(S) - 1:
                res += S[i]
            return res
        previous_string = S
        removed_string = remove_once(S)
        while removed_string != previous_string:
            previous_string = removed_string
            removed_string = remove_once(previous_string)
        return removed_string
