from math import pow

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        total = len(S)
        if total < 3:
            return []

        if S[0] == '0' and S[1] == '0':
            for item in S:
                if item != '0':
                    return []
            return [0] * len(S)

        if S[0] == \"0\":
            first_index = 0
            for second_index in range(first_index+1, total-1):
                result = [0, int(S[1:second_index+1])]
                if self.do_calc(S, second_index+1, total, result):
                    return result
            return []


        for first_index in range(0, total - 2):
            if S[first_index+1] == \"0\":
                result = [int(S[:first_index+1]), 0]
                if self.do_calc(S, first_index+2, total, result):
                    return result
                continue

            for second_index in range(first_index+1, total-1):
                result = [int(S[:first_index+1]), int(S[first_index+1:second_index+1])]
                if self.do_calc(S, second_index+1, total, result):
                    return result
        return []

    def do_calc(self, S, current_index, total, result):
        if current_index >= total:
            return True

        new_value = (result[-1] + result[-2])
        new_value_str = str(new_value)
        new_value_len = len(new_value_str)
        S_value = S[current_index:current_index+new_value_len]
        if S_value == new_value_str and new_value <= pow(2, 31) -1:
            result.append(new_value)
            return self.do_calc(S, current_index + new_value_len, total, result)
        return False
