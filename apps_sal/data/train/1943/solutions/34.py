def intersection(a: List, b: List) -> List:
    l = max(a[0], b[0])
    r = min(a[1], b[1])
    if l <= r:
        return [l, r]
    else:
        return None


def union(a: List, b: List) -> List:
    l = min(a[0], b[0])
    r = max(a[1], b[1])
    i = intersection(a, b)
    if i:
        return [l, r]
    else:
        return None


class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        while A and B:
            a = A[0]
            b = B[0]
            i = intersection(a, b)
            if i:
                result.append(i)
            if a[1] < b[1]:
                A.pop(0)
            elif a[1] > b[1]:
                B.pop(0)
            else:
                A.pop(0)
        i = 1
        while i < len(result):
            u = union(result[i - 1], result[i])
            if u:
                result.pop(i - 1)
                result.pop(i - 1)
                result.insert(i - 1, u)
            else:
                i += 1
        return result
