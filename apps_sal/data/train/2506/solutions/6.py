class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        current_s = s[0]
        current_t = t[0]
        switch_s = 0
        switch_t = 0
        s_dict = dict()
        t_dict = dict()
        for i in range(1, len(s)):
            if s[i] != current_s:
                current_s = s[i]
                switch_s += 1
            if t[i] != current_t:
                current_t = t[i]
                switch_t += 1
            if s[i] in s_dict:
                if s_dict.get(s[i]) != t[i]:
                    return False
            if t[i] in t_dict:
                if t_dict.get(t[i]) != s[i]:
                    return False
            s_dict.update({current_s: current_t})
            t_dict.update({current_t: current_s})
            if switch_s != switch_t:
                return False
        return True
