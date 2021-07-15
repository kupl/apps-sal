class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        #the output list
        res = [0] * len(puzzles)
        
        #set up the trie using dictionary
        dic = {}
        for word in words:
            cur = dic
            for letter in sorted(set(word)):
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            # if only this word contains all the letters along the branch
            if '*' not in cur:
                cur['*'] = 1
                
            # if there exists other words that contain all the 
            # letters along the branch
            else:
                cur['*'] += 1
        
        # search the trie using depth first search;
        # check_head checks whether the first letter of puzzle is in the word
        def dfs(dic, i, check_head):
            p = puzzles[i]
            if '*' in dic and check_head:
                # add the number of words that meet the specification to the                        
\t\t\t\t# corresponding position of puzzle
                res[i] += dic['*']
            for key in dic:
                if key in p:
                    if p[0] == key or check_head:
                        dfs(dic[key], i, True)
                    else:
                        dfs(dic[key], i, False)
            else:
                return
        
        # run dfs for all puzzles
        for i in range(len(puzzles)):
            dfs(dic, i, False)
        
        
        # return result
        return res     
