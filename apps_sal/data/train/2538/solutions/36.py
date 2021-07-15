class Solution:
    def countLargestGroup(self, n: int) -> int:
        num_dict = {}
        for i in range(1, n+1):
            arr = [int(a) for a in str(i)]
            summa = sum(arr)
            if summa not in num_dict.keys():
                num_dict[summa] = [i]
            else:
                num_dict[summa] = num_dict[summa] + [i]
        large = 0
        for j in num_dict.values():
            if len(j)>large:
                large = len(j)
        count = 0
        for j in num_dict.values():
            if len(j) == large:
                count += 1
        return count
