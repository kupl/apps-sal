class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        i = label
        lst = []
        while i >= 1:
            lst.append(i)
            i = i // 2
        n = len(lst)
        lst = lst[::-1]
        print(lst)
        for i in range(n):
            if n % 2 == 1:
                if i % 2 == 1:
                    lst[i] = 2 ** i + 2 ** (i + 1) - 1 - lst[i]
            elif i % 2 == 0:
                lst[i] = 2 ** i + 2 ** (i + 1) - 1 - lst[i]
        return lst
