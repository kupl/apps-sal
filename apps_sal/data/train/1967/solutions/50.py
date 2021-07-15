class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def isFib(i, a, b, count):
            if i == len(S):
                return [] if count >= 3 else None
            if a > (1<<31) - 1 or b > (1<<31) - 1 or a + b > (1<<31):
                return None
            if S[i:i+1] == ['0'] and a != 0:
                return False
            j = i + len(str(a))
            if S[j:j+1] == ['0'] and b != 0:
                return False
            if S[i:i+len(str(a+b))] != str(a+b):
                return False
            rest =  isFib(i+ len(str(a+b)), b, a+b, count + 1)
            if rest or rest == []:
                return [a+b] + rest
        
        for len_a in range(1, len(S)):
            for len_b in range(1, len(S)):
                str_a  = S[:len_a]
                str_b  = S[len_a:len_a + len_b]
                a, b = int(str_a), int(str_b)
                if a > (1<<31) - 1 or b > (1<<31) - 1:
                    continue
                if (str_a[0] == '0' and len_a > 1) or (str_b[0] == '0' and len_b > 1):
                    continue
                val = isFib(len_a + len_b, int(S[:len_a]), int(S[len_a:len_a + len_b]), 2 )
                if val: return [int(str_a), int(str_b)] + val
                if S[0] == '0':
                    break
        return []
