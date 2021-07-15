class Solution:
     def removeComments(self, source):
         """
         :type source: List[str]
         :rtype: List[str]
         """
         return [ code for code in re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n') if len(code) > 0 ]
