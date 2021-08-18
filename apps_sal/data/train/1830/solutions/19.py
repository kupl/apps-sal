class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        output = [-1] * len(rains)

        dic = dict()
        stack = []

        for i, n in enumerate(rains):
            if n == 0:
                stack.append(i)
            elif n not in dic:
                dic[n] = i
            else:
                if not stack:
                    return []

                for j in stack:
                    if j > dic[n]:
                        break

                if j < dic[n]:
                    return []
                stack.pop(stack.index(j))
                output[j] = n
                dic[n] = i

        for j in stack:
            output[j] = 1

        return output
