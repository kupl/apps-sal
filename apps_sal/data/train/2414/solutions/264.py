class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,len(arr)):
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                answer+=1
        return answer

