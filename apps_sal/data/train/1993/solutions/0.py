import re


class Solution:

    def removeComments(self, source):
        """
            :type source: List[str]
            :rtype: List[str]
            """
        lines = re.sub('//.*|/\\*(.|\n)*?\\*/', '', '\n'.join(source)).split('\n')
        return [line for line in lines if line]
