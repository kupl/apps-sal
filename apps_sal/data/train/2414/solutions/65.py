class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        perm = combinations(arr, 3)
        answer = []
        for i in perm:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and abs(i[0] - i[2]) <= c:
                answer.append(i)

        return len(answer)
