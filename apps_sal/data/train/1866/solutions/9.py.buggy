def justify_line(line, max_width):
     line_length = sum((len(i) for i in line))
     space_left = max_width - line_length
     if len(line) == 1:
         spaced_line = [line[0], " " * space_left]
     else:
         spaced_line = [line[0]]
         (spaces_per_word, remainder) = divmod(space_left, len(line) - 1)
         for i in range(1, len(line)):
             num_spaces = spaces_per_word
             if remainder > 0:
                 num_spaces += 1
                 remainder -= 1
             spaced_line.append(" " * num_spaces)
             spaced_line.append(line[i])
     return "".join(spaced_line)
 
 class Solution:
     def fullJustify(self, words, maxWidth):
         """
         :type words: List[str]
         :type maxWidth: int
         :rtype: List[str]
         """
         lines = []
         i = 0
         line = []
         line_length = 0
         while i < len(words):
             if line_length != 0:
                 line_length += 1
             line_length += len(words[i])
             if line_length <= maxWidth:
                 line.append(words[i])
                 i += 1
             else:
                 lines.append(justify_line(line, maxWidth))
                 line = []
                 line_length = 0
         if line:
             final_line = " ".join(line)
             final_line += " " * (maxWidth - len(final_line))
             lines.append(final_line)
         return lines
