class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        answers = []

        queue = [list(range(1, N + 1))]
        while queue:
            ls = queue.pop()
            if len(ls) > 2:
                odd = []
                even = []

                for i, val in enumerate(ls):
                    if i % 2:
                        odd.append(val)
                    else:
                        even.append(val)

                queue.append(odd)
                queue.append(even)
            else:
                answers += ls

        return answers
