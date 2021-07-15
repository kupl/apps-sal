class Solution:
    def reformat(self, s: str) -> str:
        chars = []
        nums = []
        for i in s:
            try:
                nums.append(int(i))
            except ValueError:
                chars.append(i)
        if abs(len(nums)-len(chars)) > 1:
            return ''
        
        out = [0]*len(s)
        if len(nums) >= len(chars):
            out[::2], out[1::2] = nums, chars
        else:
            out[::2], out[1::2] = chars,nums
            
        
        return ''.join([str(i) for i in out])
