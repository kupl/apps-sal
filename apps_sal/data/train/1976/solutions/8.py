class MagicDictionary:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.d = None
 
     def buildDict(self, dict):
         """
         Build a dictionary through a list of words
         :type dict: List[str]
         :rtype: void
         """
         d=set()
         for word in dict:
             d.add(word)
         self.d = d
         
     def search(self, word):
         """
         Returns if there is any word in the trie that equals to the given word after modifying exactly one character
         :type word: str
         :rtype: bool
         """
         if not word:
             return
         
         def editDistDP(s1, s2):
             m, n = len(s1), len(s2)
             dp = [[0 for x in range(n+1)] for x in range(m+1)]
             for i in range(m+1):
                 for j in range(n+1):
                     if i == 0:
                         dp[i][j] = j    # Min. operations = j
                     elif j == 0:
                         dp[i][j] = i    # Min. operations = i
                     # If last characters are same, ignore last char
                     # and recur for remaining string
                     elif s1[i-1] == s2[j-1]:
                         dp[i][j] = dp[i-1][j-1]
                         # If last character are different, consider all
                     # possibilities and find minimum
                     else:
                         dp[i][j] = 1 + dp[i-1][j-1]
             return dp[m][n]
         # print(self.d)
         ans = False
         for dic in self.d:
             if len(dic) != len(word):
                 continue
             ans = ans or editDistDP(dic, word)==1
         return ans
 
 # Your MagicDictionary object will be instantiated and called as such:
 # obj = MagicDictionary()
 # obj.buildDict(dict)
 # param_2 = obj.search(word)

