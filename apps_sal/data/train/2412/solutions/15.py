class Solution:
    def removeDuplicates(self, S: str) -> str:
        str_list = []
        for i in range(len(S)):
            str_list.append(S[i])

        i = 0
        while i < len(str_list) - 1:
            if str_list[i] == str_list[i + 1]:
                del(str_list[i])
                del(str_list[i])
                if i > 0:
                    i -= 1
            else:
                i += 1

        str_end = ''
        for i in range(len(str_list)):
            str_end += str(str_list[i])
        return str_end
