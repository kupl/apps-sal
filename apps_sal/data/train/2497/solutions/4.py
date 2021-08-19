class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                toCheck = arr[i:i + 3]
                print(toCheck)
                if len(toCheck) >= 3:
                    if toCheck[1] % 2 != 0 and toCheck[2] % 2 != 0:
                        return True
        return False
