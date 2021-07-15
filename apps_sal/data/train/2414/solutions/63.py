class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        combs = combinations(arr, 3)
        fin = []
        for i in combs:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and abs(i[0] - i[2]) <= c:
                fin.append(i)
                    
        return len(fin)
