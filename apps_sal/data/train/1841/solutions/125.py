class Solution:
    def getStrongest1(self, arr: List[int], k: int) -> List[int]:
        # sort, find median per definition
        # iterate backwards over sorted list
        # abs(diff from median) used as key in hashmap, with element as value
        # this naturally places larger values first in {key, [vals]}
        # starting from largest key, return K values
        # O(NlogN) time, O(N) space

        arr.sort()
        m = arr[(len(arr) - 1) // 2]

        d = {}
        for i in range(len(arr) - 1, -1, -1):
            tmp = abs(arr[i] - m)
            d.setdefault(tmp, [])
            d[tmp].append(arr[i])

        res = []
        for key in sorted(d.keys(), reverse=True):
            res.extend(d[key])
            if len(res) >= k:
                break
        return res[:k]

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # same initial strategy to find median
        # but afterward use two pointers to build up result list
        # terminating on K elements
        # O(NlogN) time, O(1) \"extra\" space not counting result list

        arr.sort()
        la = len(arr)
        m = arr[(la - 1) // 2]
        i, j, res = 0, la - 1, []

        while len(res) < k:
            rt = abs(arr[j] - m)
            lt = abs(arr[i] - m)

            if rt == lt or rt > lt:
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
        return res
