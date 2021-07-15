class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans=[]
        for i in range(len(arr)):
            # taking the remaining elements of arr into A, excluding upto i 
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j])<=a:
                    # taking the remaining elements of A into B, excluding upto j
                    for k in range(j+1,len(arr)):
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                ans.append((arr[i],arr[j],arr[k]))
        return len(ans)

