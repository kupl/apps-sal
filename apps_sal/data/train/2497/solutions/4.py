class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        # Walk through the list
        # stop at an odd number
        # are the next 2 odd?
        # if so, yes and return
        # if not, walk forward one and try again

        for i in range(len(arr)):
            # I found an odd, are the next two odd?
            if arr[i] % 2 != 0:
                toCheck = arr[i: i + 3]

                print(toCheck)
                if len(toCheck) >= 3:
                    if toCheck[1] % 2 != 0 and toCheck[2] % 2 != 0:
                        return True

        return False
