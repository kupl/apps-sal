class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        dict_a = defaultdict(set)
        dict_b = defaultdict(set)
        dict_c = defaultdict(set)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    dict_a[i].add(j)
                if abs(arr[i] - arr[j]) <= b:
                    dict_b[i].add(j)
                if abs(arr[i] - arr[j]) <= c:
                    dict_c[i].add(j)

        for i in range(len(arr) - 2):
            for j in dict_a[i]:
                for k in dict_b[j]:
                    if k in dict_c[i]:
                        count = count + 1
        return count
