class Solution:
    def maximum69Number(self, num: int) -> int:
        lst = list(map(int, str(num)))
        for i in range(len(lst)):
            if lst[i] == 6:
                lst[i] = 9
                break
        return int(''.join(map(str, lst)))
