def merge(L,R):
    if len(L)==0:
        return R
    if len(R)==0:
        return L
    l=0
    r=0
    res=[]
    while len(res)<len(L)+len(R):
        if L[l]<R[r]:
            res.append(L[l])
            l+=1
        else:
            res.append(R[r])
            r+=1
        if l==len(L):
            res+=R[r:]
            break
        if r==len(R):
            res+=L[l:]
            break
    return res
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        mid=len(nums)//2
        L=self.sortArray(nums[:mid])
        R=self.sortArray(nums[mid:])
        return merge(L,R)

