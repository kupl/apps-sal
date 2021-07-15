class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        w1_set = {}
        for word in B:
            new_w1_set = {}
            for c in word:
                if c not in new_w1_set:
                    new_w1_set[c] = 0
                new_w1_set[c] += 1
                
            for c in new_w1_set:
                if c not in w1_set:
                    w1_set[c] = new_w1_set[c]
                else:
                    w1_set[c] = max(w1_set[c], new_w1_set[c])
        
        output = []
        for word in A:
            w2_set = {}
            for c in word:
                if c not in w2_set:
                    w2_set[c] = 0
                w2_set[c] += 1
            
            check = True
            for c in w1_set:
                if (c not in w2_set) or (w1_set[c] > w2_set[c]):
                    check = False
                    break
            
            if check:
                output.append(word)
            
        return output

