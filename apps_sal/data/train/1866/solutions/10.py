class Solution:
     def fullJustify(self, words, maxWidth):
         """
         :type words: List[str]
         :type maxWidth: int
         :rtype: List[str]
         """
         
         acc = 0 # number of letters
         tmp, res = [], []
         for w in words:
             if acc + len(w) + len(tmp) > maxWidth:
                 # make up a line
                 for i in range(maxWidth - acc):
                     tmp[i%(len(tmp)-1 or 1)] += ' ' # need or 1 for the case: one word in tmp [to] --> "to    "
                 res.append(''.join(tmp))
                 acc = 0
                 tmp = []
                 
             tmp.append(w)
             acc += len(w)
             
         # the last element
         return res + [' '.join(tmp).ljust(maxWidth)]
                 

