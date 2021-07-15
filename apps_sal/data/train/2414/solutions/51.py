class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pointer1 = 0
        pointer2 = 1
        pointer3 = 2

        res = 0

        length = len(arr)

        while pointer1 < length - 2:
            while pointer2 < length - 1:
                while pointer3 < length:
                    if abs(arr[pointer1]-arr[pointer2]) <= a and abs(arr[pointer2]-arr[pointer3]) <=b and abs(arr[pointer1]-arr[pointer3]) <=c:
                        res += 1
                    pointer3+=1
                pointer2+=1
                pointer3=pointer2+1
            pointer1+=1
            pointer2 = pointer1+1
            pointer3 = pointer2+1

        return(res)
