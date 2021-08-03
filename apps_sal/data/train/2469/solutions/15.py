class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubledList = []
        l = len(arr)
        for num in arr:
            doubledList.append(num * 2)
        for i in range(l):
            if doubledList[i] in arr and arr.index(doubledList[i]) != i:
                return True
        return False
