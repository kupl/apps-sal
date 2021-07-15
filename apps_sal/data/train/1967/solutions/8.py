class Solution:
    def trysolve(self, s, seq, n):
        seq.append(n)
        if self.solve(s, seq):
            return True
        seq.pop()
        return False
       
    def solve(self, s, seq):
        if not s:
            return True
        target = sum(seq[-2:])
        if target > 2 ** 31 - 1:
            return False
        if s[0] == '0':
            if target == 0:
                return self.trysolve(s[1:], seq, 0) ;
            else:
                return False
        for end in range(1, len(s)+1):
            n = int(s[:end])
            if n == target and self.trysolve(s[end:], seq, n):
                return True
        return False       
     
    def splitIntoFibonacci(self, S: str) -> List[int]:
        limit = 2**31 - 1;
        for i in range(1, len(S)):
            n1 = int(S[:i]);
            if(n1>limit):
                return [];
            if(n1!=0 and S[0]=='0'):
                return [];
            for j in range(i+1, len(S)):
                n2 = int(S[i:j])
                if n2 != 0 and S[i] == '0':
                    break
                if n2 > limit:
                    break 
                seq = [n1, n2]
                if self.solve(S[j:], seq):
                    return seq;
        return []
                
            

