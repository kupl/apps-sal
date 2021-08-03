class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # if not sol return []

        # start from target and trace back, use dfs each time change slice in stamp to ??? or ??X

        list_s, list_t = list(stamp), list(target)  # convert to list coz str immutable
        res = []

        # changed means if this round can remove stamp
        changed = True
        while changed:
            # 记住先赋值false！！！
            changed = False
            # check each slice of target if can remove stamp!
            for i in range(len(list_t) - len(list_s) + 1):
                changed = changed or self.remove_stamp(list_s, list_t, i, res)

        return res[::-1] if list_t == ['?'] * len(list_t) else []

    def remove_stamp(self, list_s, list_t, i, res):
        # check if target can remove stamp from ind of i; if ? can also remove!!!!!!!(abc??-->ababc 反过来 ababc-->ab??? then ab? can still un-stamp!!!!)
        changed = False

        for j in range(len(list_s)):
            if list_t[i + j] == '?':
                continue
            if list_t[i + j] != list_s[j]:
                return False
            changed = True

        # also need convert target back!
        if changed:
            list_t[i:i + len(list_s)] = ['?'] * len(list_s)  # 数组可以直接整体赋值！！！

            res.append(i)

        return changed
