class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        even_set = []
        odd_set = []
        for i in A:
            even = []
            odd = []
            for j in range(len(i)):
                if j % 2 == 0:
                    even.append(i[j])
                else:
                    odd.append(i[j])
            even.sort()
            odd.sort()
            if even in even_set:
                k = []
                for p, values in enumerate(even_set):
                    if even == values:
                        k += [p]
                flag = 0
                for p in k:
                    if odd_set[p] == odd:
                        flag = 1
                        break
                if flag == 0:
                    even_set.append(even)
                    odd_set.append(odd)
            else:
                even_set.append(even)
                odd_set.append(odd)

        return len(even_set)
