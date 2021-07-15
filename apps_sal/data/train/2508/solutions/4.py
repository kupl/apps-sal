class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # my method 2: counting sort and compare difference O(n+r): r number of max_value O(n); only works for small numbers sorting
        
        maxVal = max(heights)
        
        # create frequency table for each digit from 0 to maxVal
        freq = [0] * (maxVal + 1)
        # get freq for all index
        for num in heights:
            freq[num] += 1
        # acc index by num[i] += num[i-1]
        for i in range(1,len(freq)):
            freq[i] += freq[i-1]
            
        # loop heights, find its freq and index back in places
        places = [0] * len(heights)
        for num in heights:
            # num has freq[num] th in ranking, but -1 to be index
            places[freq[num]-1] = num
            freq[num] -= 1
        
        ans = 0
        for i in range(len(heights)):
            if heights[i] != places[i]:
                ans += 1
        return ans
            

