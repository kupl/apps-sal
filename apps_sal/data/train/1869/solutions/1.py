class Solution:
    ''' Transform the input into following format:
        [ ... ,(num, num_level), ...]
        example: \"1-2--3--4-5\" -> [(1,0), (2,1), (3,2), (4,2), (5,1)]
    '''
    def __transform(self, S):
        split = S.split('-')
        index = 1
        res = [(split[0], 0)]
        while index < len(split):
            level = 0
            if split[index] == '':
                while split[index] == '':
                    level +=1
                    index +=1
            num = int(split[index])
            res.append((num, level+1))
            index += 1
        return res
    def recoverFromPreorder(self, S: str) -> TreeNode:
        L = {}
        trans_input = self.__transform(S)
        L[0] = TreeNode(trans_input[0][0], None, None)
        for num,level in trans_input[1:]:
            L[level] = TreeNode(num, None, None)
\t\t\t# Check if left of last level is mapped, ow map to right of last level.
            if not L[level-1].left:
                L[level-1].left = L[level]
            else:
                L[level-1].right = L[level]
        return L[0]
