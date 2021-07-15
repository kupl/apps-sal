class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count =0
        for i in arr1 :
            new_list= list([abs(m -i) for m in arr2])
            if all(x>d for x in new_list):
                count += 1
        return count
            

