from typing import List
class Solution:
    def strengths(self,arr,length):
      ans = []
      m = arr[(length-1)//2]
      for i in arr:
        ans.append(abs(m-i))
      return ans
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
      length = len(arr)
      if length==1:
        return arr
      ans = []
      arr.sort()
      strength = self.strengths(arr,length)
      count = 0
      i = 0
      a = length - 1
      while count < k and i != a:
        # print(count,k)
        if strength[a] > strength[i]:
          ans.append(arr[a])
          a -= 1
        elif strength[a] < strength[i]:
          ans.append(arr[i])
          i += 1
        else:
          if arr[a] > arr[i]:
            ans.append(arr[a])
            a -= 1
          else:
            ans.append(arr[i])
            i += 1
        count += 1
      if count < k and i==a:
        ans.append(arr[(length-1)//2])
      return ans
        

