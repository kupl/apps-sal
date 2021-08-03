class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        l = list(A[0])

        for i in A:
            for j in range(len(i)):
                if l[j] == 'A':
                    continue
                if i[j] < l[j]:
                    l[j] = 'A'
                else:
                    l[j] = i[j]
                # print(l)
        # print(l)
        return l.count('A')
