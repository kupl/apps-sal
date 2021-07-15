class Solution:
     def removeComments(self, source):
         """
         :type source: List[str]
         :rtype: List[str]
         """
         t = '\n'.join(source)
         
         p = re.compile(r'//.*|/\*(.|\n)*?\*/')
         
         t = p.sub('', t)
         
         return list(filter(None, t.split('\n')))
