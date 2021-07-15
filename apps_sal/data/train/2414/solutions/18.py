class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        length = len(arr)
        for i in range(0, length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if abs(arr[i] - arr[j]) <=a and abs(arr[j]- arr[k])<= b and abs(arr[i]- arr[k])<= c:
                        count += 1
        return count
