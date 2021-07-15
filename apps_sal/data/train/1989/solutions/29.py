class Solution:
    def longestAwesome(self, s: str) -> int:
        '''
        \"3242415\"
        
          9876543210
        0:0000000000    #ith digit is odd
        1:0000001000
        2:0000001100
        3:0000011100
        4:0000011000
        5:0000001000
        6:0000001010
        7:0000101010
        
        
        2: need 0000001100, 0000001101, 0000001110, ...
            add 0000001100
        '''
        digit_cnt = [0 for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            digit_cnt[i] = digit_cnt[i-1] ^ (1<<int(s[i-1]))
        # print(digit_cnt)
        
        res = 1
        indx = {}
        indx[0] = 0
        for i in range(1, len(digit_cnt)):
            if digit_cnt[i] == 0: 
                res = max(res, i)
                continue
            for d in range(10):
                if digit_cnt[i] ^ (1<<d) in list(indx.keys()):
                    res = max(res, i-indx[digit_cnt[i] ^ (1<<d)])
            if not digit_cnt[i] in list(indx.keys()):
                indx[digit_cnt[i]] = i
        # print(indx)
        return res
        
        

