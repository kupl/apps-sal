class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if arr[0] == 0 and arr[1] == 0:
            return True
        dictionary = {}
        for number in arr:
            dictionary[2 * number] = True
        for number in arr:
            if number in dictionary and number != 0:
                return True
        return False
