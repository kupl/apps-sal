class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        output_list = []
        def count(word):
            res = [0] * 26
            for ch in word:
                pos = ord(ch) - ord('a')
                res[pos] = res[pos] + 1
            return res
        
        b_max = [0]*26
        for b in B:
            res_b = count(b)
            for i in range(26):
                b_max[i] = max(b_max[i], res_b[i])
        #print(b_max)
        for a in A:
            #Following is one simple way to compare two lists
            '''res_a = count(a)
            for i in range(26):
                if b_max[i] > res_a[i]:
                    break
                if i == 25:
                    output_list.append(a)'''
            #Following is another zip function way to compare two list(or iterators)
            if all(x>=y for x,y in zip(count(a), b_max)):
                output_list.append(a)            
        return output_list
                    
                
            
        
        

