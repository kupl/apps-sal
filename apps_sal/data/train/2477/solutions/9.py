class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        lst = [string2IndRes(string) for string in A]
        u_lst = unique(lst)
        return len(u_lst)


def string2IndRes(string):
    res = []
    for (i, c) in enumerate(string):
        res.append((c, i % 2))
    return Counter(res)


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
