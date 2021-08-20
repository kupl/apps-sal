class Solution:

    def average(self, salary: List[int]) -> float:
        s = salary[:]
        max_ind = 0
        min_ind = 0
        for i in range(1, len(s)):
            if s[max_ind] < s[i]:
                max_ind = i
            elif s[min_ind] > s[i]:
                min_ind = i
        print((max_ind, min_ind))
        if max_ind < min_ind:
            del s[max_ind]
            del s[min_ind - 1]
        else:
            del s[min_ind]
            del s[max_ind - 1]
        return sum(s) / len(s)
