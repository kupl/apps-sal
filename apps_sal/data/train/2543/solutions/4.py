class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        (read_index, write_index) = (len(S) - 1, 0)
        res = list(S)
        while read_index >= 0:
            c = S[read_index]
            if not c.isalpha():
                read_index -= 1
                continue
            while not res[write_index].isalpha():
                write_index += 1
            res[write_index] = c
            read_index -= 1
            write_index += 1
        return ''.join(res)
