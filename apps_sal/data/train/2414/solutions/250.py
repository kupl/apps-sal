class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pair = {p: dict() for p in (a, b, c)}
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(arr[i] - arr[j])
                for p in (a, b, c):
                    if d <= p:
                        if i not in pair[p]:
                            pair[p][i] = set()
                        pair[p][i].add(j)
        ans = 0
        empty = set()
        for i, js in pair[a].items():
            for j in js:
                ans += len(pair[b].get(j, empty) & pair[c].get(i, empty))
        return ans
