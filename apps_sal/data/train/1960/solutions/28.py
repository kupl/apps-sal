class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        result += [queries[0] - 1]
        for (ind, q) in enumerate(queries[1:]):
            ind = ind + 1
            if q > max(queries[:ind]):
                result += [q - 1]
            else:
                equal_q = [i for i in range(ind) if q == queries[i]]
                if len(equal_q) > 0:
                    diff = len(list(set(queries[equal_q[-1] + 1:ind])))
                    result += [diff]
                else:
                    sum_higher = len([x for x in list(set(queries[:ind])) if x > q])
                    result += [q + sum_higher - 1]
        return result
