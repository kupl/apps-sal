class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(list(B)) > set(list(A)):
            return -1

        l_b = len(B)
        pointer_b = 0
        l_a = len(A)
        pointer_a = 0

        L = []
        while pointer_a < l_a:
            if A[pointer_a] == B[pointer_b]:
                L.append(pointer_a)
            pointer_a += 1

        if L == []:
            return -1

        for pointer_a in L:
            times = 1
            while pointer_b < l_b:
                if pointer_a == l_a:
                    pointer_a = 0
                    times += 1
                if B[pointer_b] == A[pointer_a]:
                    pointer_b += 1
                    pointer_a += 1
                    continue
                else:
                    break
            if pointer_b == l_b:
                return times
            else:
                pointer_b = 0
        return -1
