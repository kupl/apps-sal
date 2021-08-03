class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        if len(A) == 1:
            return 1

        def areSpecialEquiv(x: str, y: str) -> bool:
            dic_x = {}
            dic_y = {}
            for c in x:
                if c not in y:
                    return False

            for i in range(len(x)):
                found = 0
                for j in range(len(y)):
                    if x[i] == y[j] and i % 2 == j % 2:
                        found = 1
                if not found:
                    return False

            for l in x:
                if l in dic_x:
                    dic_x[l] += 1
                else:
                    dic_x[l] = 1

            for l in y:
                if l in dic_y:
                    dic_y[l] += 1
                else:
                    dic_y[l] = 1

            for l in dic_x:
                if dic_x[l] != dic_y[l]:
                    return False

            return True

        stack = A[:]
        arr = []

        while stack:
            arr2 = []
            curr = stack.pop(0)
            count = 1

            for w in stack:
                if areSpecialEquiv(curr, w):
                    count += 1
                    arr2.append(w)
            arr.append(count)

            for i in arr2:
                stack.remove(i)

        return len(arr)
