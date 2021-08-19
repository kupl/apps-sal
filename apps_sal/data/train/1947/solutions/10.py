class Solution:

    def subset(self, a, b):
        base = [0] * 26
        i = 0
        while i < len(a) or i < len(b):
            if i < len(a) and i < len(b):
                base[ord(a[i]) - 97] -= 1
                base[ord(b[i]) - 97] += 1
            elif i < len(a):
                base[ord(a[i]) - 97] -= 1
            else:
                return False
            i += 1
        for c in base:
            if c > 0:
                return False
        return True

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B = list(set(B))
        base = [0] * 26
        for b in B:
            cur = [0] * 26
            for c in b:
                cur[ord(c) - 97] += 1
            for i in range(len(base)):
                base[i] = max(base[i], cur[i])
        ret = []
        for a in A:
            cur = [0] * 26
            for c in a:
                cur[ord(c) - 97] += 1
            add = True
            for i in range(len(base)):
                if base[i] > cur[i]:
                    add = False
                    break
            if add:
                ret.append(a)
        return ret
