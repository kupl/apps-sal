import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_dict = collections.defaultdict(list)
        max_curr = 0
        answer = 0
        
        def get_digit_sum(num):
            return sum(int(i) for i in [char for char in str(num)])
        
        for i in range(1, n+1):
            digit_sum_curr = get_digit_sum(i)
            digit_dict[digit_sum_curr].append(i)
            
            if len(digit_dict[digit_sum_curr]) > max_curr:
                max_curr = len(digit_dict[digit_sum_curr]) 
                answer = 1
            elif len(digit_dict[digit_sum_curr]) == max_curr:
                answer += 1
                
        return answer
            

