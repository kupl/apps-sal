class Solution:
    def wordSubsets(self, A, B):
        def count_word(word):
            a = [0] * 26
            
            for c in word:
                a[ord(c) - ord(\"a\")] += 1
            
            return a
        
        max_count = [0] * 26
        
        for w in B:
            cur_count = count_word(w)
            max_count = [max(cur_count[i], max_count[i]) for i in range(len(cur_count))]
            
        ans = []
        for w in A:
            if all(x>=y for x,y in zip(count_word(w), max_count)):
                ans.append(w)
        
        return ans
