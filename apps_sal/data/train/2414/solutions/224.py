def bruteforce(arr, a, b, c):
    count = 0
    for i in range(len(arr) - 2):
        arri = arr[i]
        for j in range(i+1, len(arr) - 1):
            if abs(arri - arr[j]) > a:
                continue
            arrj = arr[j]
            for k in range(j+1, len(arr)):
                if abs(arrj - arr[k]) <= b and abs(arri - arr[k]) <= c:
                    count += 1
    return count
                           
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return bruteforce(arr, a, b, c)
