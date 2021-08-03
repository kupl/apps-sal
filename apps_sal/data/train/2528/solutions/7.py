class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ############MY SOLUTION############################
        #import numpy as np
        #pref = ""
        #i = 0
        #stop = 0

        # if not all(strs): #empty str
        #    return("")

        # while not stop:
        #    letter = np.unique([l[i:(i+1)] for l in strs])
        #    if len(letter) == 1 and letter[0] != "" :
        #        pref += letter[0]
        #        i += 1
        #    else:
        #        stop = 1
        # return(pref)

        ###########OTHER##################################
        if not strs:  # if strs = []
            return("")

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return(strs[0][:i])

        # if shortest string is the common prefix or strs contains ""
        else:
            return(min(strs))
