class Solution:
    def recurse(self, prev_digit: int, remaining:int, k:int) -> List[List[int]]:
        if remaining == 0:
            raise Exception()
        curr_digits = set(filter(lambda d: d>=0 and d<10, [prev_digit+k, prev_digit-k]))
        ret = []
        for curr_digit in curr_digits:
            if remaining > 1:
                nums = self.recurse(curr_digit, remaining-1, k)
                for num in nums:
                    # print('num', num)
                    new_num = [curr_digit]+num
                    # print('new_num', new_num)
                    ret.append(new_num)
            else:
                ret.append([curr_digit])
        
        # print(prev_digit, ret)
        return ret
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ret = []
        for d in range(1, 10):
            nums = self.recurse(d, n-1, k)
            for num in nums:
                new_num = [d]+num
                ret.append(new_num)
        ret = list(filter(lambda l: len(l)==n, ret))
        ret = list(map(lambda l: [str(c) for c in l], ret))
        return [\"\".join(num) for num in ret]
