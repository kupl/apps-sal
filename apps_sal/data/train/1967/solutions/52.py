class Solution:
    def validFib(self, S, n1, n2, i, ret):
        
        if (n1[0] != '0' and len(n1) >= 1) or n1 == '0':
            num1 = int(n1)
        else:
            return False
        if (n2[0] != '0' and len(n2) >= 1) or n2 == '0':
            num2 = int(n2)
        else:
            return False
        
        num3 = num1 + num2
        # if num1 == 123 and num2 == 456:
        #     print(num3, i)
        n3 = str(num3)
        
        j = 0
        while j + i < len(S) and j < len(n3):
            c1 = n3[j]
            c2 = S[j+i]
            if c1 != c2:
                return False
            j += 1
        
        if len(n1) + len(n2) + len(n3) > len(S):
            return False
        
        if i + len(n3) == len(S) and num3 <= 2**31 - 1:
            ret.append(str(num3))
            return True
        
        if self.validFib(S, n2, n3, i+len(n3), ret) and num3 <= 2**31 - 1:
            ret.append(str(num3))
            return True
        
        return False
    
    
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        ret = []
        
        # print(\"01\".isnumeric())
        
        i = 0
        while i < len(S):
            j = 1
            while i + j < len(S):
                n1 = S[ : i+1]
                n2 = S[i+1 : i+j+1]
                # print(n1, n2)
                if self.validFib(S, n1, n2, i+j+1, ret):
                    ret.append(n2)
                    ret.append(n1)
                    return reversed(ret)
                
                j += 1
            i += 1
        
        return []
