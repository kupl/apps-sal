class Solution(object):
     def fullJustify(self, words, maxWidth):
         """
         :type words: List[str]
         :type maxWidth: int
         :rtype: List[str]
         """
         res, line, length_of_line = [], [], 0
         for word in words:
             if length_of_line + len(word) + len(line) > maxWidth:
                 #build a line to be printed, and append into res
                 for idx in range(maxWidth - length_of_line):
                     #add a blank to which word in a line
                     word_idx = idx % ((len(line) - 1) or 1)
                     line[word_idx] += ' '
                 res.append(''.join(line))
                 line, length_of_line = [], 0
             length_of_line += len(word)
             line.append(word)
         return res + [' '.join(line).ljust(maxWidth)]

