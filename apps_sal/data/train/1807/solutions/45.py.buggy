class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def frac_to_string(num, den):
            return f\"{num}/{den}\"
        
        def relatively_prime(a, b):
            \"\"\" Invariant: a < b \"\"\"
            for i in range(2, a + 1):
                if a % i == 0 and b % i == 0:
                    return False
            return True
        
        ans = []
        for den in range(1, n + 1):
            for num in range(1, den):
                if relatively_prime(num, den):
                    ans.append(frac_to_string(num, den))
        return ans
        
