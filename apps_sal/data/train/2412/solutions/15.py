class Solution:
    def removeDuplicates(self, S: str) -> str:
        # преобразовываем строку в список
        str_list = []
        for i in range(len(S)):
            str_list.append(S[i])
        
        # убираем дубли
        i = 0
        while i < len(str_list)-1:
            if str_list[i] == str_list[i+1]:
                del(str_list[i])
                del(str_list[i])
                if i > 0: i -= 1
            else:
                i += 1
        
        # преобразовываем обратно в строку
        str_end = ''
        for i in range(len(str_list)):
            str_end += str(str_list[i])
        return str_end

