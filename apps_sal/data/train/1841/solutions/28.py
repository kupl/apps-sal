class Solution:
\tdef getStrongest(self, arr: List[int], k: int) -> List[int]:
\t\tmedian = sorted(arr)[(len(arr)-1)//2]
\t\treturn sorted(arr,key = lambda x: [abs(x-median),x],reverse=True )[:k]
