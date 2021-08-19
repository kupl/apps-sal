class Solution:

    def sortString(self, s: str) -> str:
        new_list = []
        temp_list = list(s)
        while len(temp_list) > 0:
            if len(temp_list) == 0:
                break
            else:
                slist = sorted(temp_list)
                temp_list = []
                new_list.append(slist.pop(0))
                for i in slist:
                    if ord(i) == ord(new_list[-1]):
                        temp_list.append(i)
                    if ord(i) > ord(new_list[-1]):
                        new_list.append(i)
            if len(temp_list) == 0:
                break
            else:
                slist = sorted(temp_list, reverse=True)
                temp_list = []
                new_list.append(slist.pop(0))
                for i in slist:
                    if ord(i) == ord(new_list[-1]):
                        temp_list.append(i)
                    if ord(i) < ord(new_list[-1]):
                        new_list.append(i)
        return ''.join(new_list)
